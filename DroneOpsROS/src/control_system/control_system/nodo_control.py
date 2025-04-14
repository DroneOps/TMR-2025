#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import math

# ROS message imports
from std_msgs.msg import Int32MultiArray
from sensor_msgs.msg import Imu
from mavros_msgs.msg import AttitudeTarget  # MAVROS message type for attitude setpoints
from geometry_msgs.msg import Quaternion

# Helper: Convert Euler angles (roll, pitch, yaw) to quaternion (black-box conversion)
def euler_to_quaternion(roll, pitch, yaw):
    """
    Convert Euler angles (in radians) to quaternion.
    """
    cy = math.cos(yaw * 0.5)
    sy = math.sin(yaw * 0.5)
    cp = math.cos(pitch * 0.5)
    sp = math.sin(pitch * 0.5)
    cr = math.cos(roll * 0.5)
    sr = math.sin(roll * 0.5)

    q = Quaternion()
    q.w = cr * cp * cy + sr * sp * sy
    q.x = sr * cp * cy - cr * sp * sy
    q.y = cr * sp * cy + sr * cp * sy
    q.z = cr * cp * sy - sr * sp * cy
    return q

# Utility: Clamp a value between low and high.
def clamp(val, low, high):
    return max(low, min(high, val))

class DroneControlEulerNode(Node):
    def __init__(self):
        super().__init__('drone_control_euler_node')

        # Declare and retrieve PID and physical parameters.
        self.declare_parameter('kp', 0.01)
        self.declare_parameter('ki', 0.001)
        self.declare_parameter('kd', 0.005)
        self.declare_parameter('mass', 1.5)          # drone mass in kg
        self.declare_parameter('thrust', 15.0)         # nominal total thrust in N
        self.declare_parameter('desired_x', 0.0)       # desired x position
        self.declare_parameter('desired_y', 0.0)       # desired y position

        self.kp = self.get_parameter('kp').value
        self.ki = self.get_parameter('ki').value
        self.kd = self.get_parameter('kd').value
        self.mass = self.get_parameter('mass').value
        self.thrust = self.get_parameter('thrust').value
        self.desired_x = self.get_parameter('desired_x').value
        self.desired_y = self.get_parameter('desired_y').value

        # Initialize PID state for both x and y axes.
        self.integral_x = 0.0
        self.integral_y = 0.0
        self.prev_error_x = 0.0
        self.prev_error_y = 0.0
        self.prev_time = self.get_clock().now().nanoseconds / 1e9

        # Latest marker measurements for x and y.
        self.marker_x = None
        self.marker_y = None

        # Latest yaw from the IMU (to maintain current heading).
        self.current_yaw = 0.0

        # Subscribers for marker data and IMU data.
        self.marker_sub = self.create_subscription(
            Int32MultiArray,
            '/marker_info',
            self.marker_callback,
            10)

        self.imu_sub = self.create_subscription(
            Imu,
            '/imu',
            self.imu_callback,
            10)

        # Publisher for attitude setpoint (to be sent to Pixhawk via MAVROS).
        self.attitude_pub = self.create_publisher(
            AttitudeTarget,
            '/mavros/setpoint_raw/attitude',
            10)

        # Timer to run the control loop at 10 Hz.
        self.timer = self.create_timer(0.1, self.control_loop)
        self.get_logger().info("Drone control Euler node started.")

    def marker_callback(self, msg: Int32MultiArray):
        """
        Processes marker info.
        Expected data layout: [marker_id, x, y, yaw].
        Uses x and y for lateral control.
        """
        data = msg.data
        if len(data) >= 4:
            self.marker_x = float(data[1])
            self.marker_y = float(data[2])
            self.get_logger().debug(f"Marker data - x: {self.marker_x}, y: {self.marker_y}")

    def imu_callback(self, msg: Imu):
        """
        Extracts yaw from the IMU message using quaternion-to-Euler conversion.
        """
        q = msg.orientation
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        yaw = math.atan2(siny_cosp, cosy_cosp)
        self.current_yaw = yaw
        self.get_logger().debug(f"IMU yaw: {math.degrees(yaw):.2f} deg")

    def control_loop(self):
        current_time = self.get_clock().now().nanoseconds / 1e9
        dt = current_time - self.prev_time
        if dt <= 0.0:
            dt = 0.1

        # Ensure we have valid marker measurements.
        if self.marker_x is None or self.marker_y is None:
            self.get_logger().warn("Marker measurements not available.")
            return

        # Calculate error for x and y axes.
        error_x = self.marker_x - self.desired_x
        error_y = self.marker_y - self.desired_y

        # Update integral terms.
        self.integral_x += error_x * dt
        self.integral_y += error_y * dt

        # Compute derivative terms.
        derivative_x = (error_x - self.prev_error_x) / dt
        derivative_y = (error_y - self.prev_error_y) / dt

        # --- Compute desired pitch (θ₍c₎) for x-axis control ---
        # Formula: θ_c = sin⁻¹{ [ kp*(x - x_c) + ki∫(x - x_c)dt + kd*(x_dot) ] * m / F_th }
        control_term_x = self.kp * error_x + self.ki * self.integral_x + self.kd * derivative_x
        theta_argument = control_term_x * self.mass / self.thrust
        theta_argument = clamp(theta_argument, -1.0, 1.0)
        theta_c = math.asin(theta_argument)

        # --- Compute desired roll (ϕ₍c₎) for y-axis control ---
        # Formula: ϕ_c = sin⁻¹{ -[ kp*(y - y_c) + ki∫(y - y_c)dt + kd*(y_dot) ] * m / ( cos(θ_c)*F_th ) }
        control_term_y = self.kp * error_y + self.ki * self.integral_y + self.kd * derivative_y
        phi_argument = - control_term_y * self.mass / (math.cos(theta_c) * self.thrust)
        phi_argument = clamp(phi_argument, -1.0, 1.0)
        phi_c = math.asin(phi_argument)

        self.get_logger().info(
            f"error_x: {error_x:.2f}, θ_c: {math.degrees(theta_c):.2f} deg | error_y: {error_y:.2f}, ϕ_c: {math.degrees(phi_c):.2f} deg"
        )

        # Build the attitude setpoint using computed Euler angles.
        # Roll (ϕ_c) and pitch (θ_c) come from our controller; yaw remains the current yaw.
        setpoint = AttitudeTarget()
        setpoint.header.stamp = self.get_clock().now().to_msg()
        setpoint.type_mask = 7  # Ignore body rates.
        # Convert Euler angles to quaternion (conversion as a "black box")
        q = euler_to_quaternion(phi_c, theta_c, self.current_yaw)
        setpoint.orientation = q

        # Set thrust (normalized value from 0.0 to 1.0; adjust as needed).
        setpoint.thrust = 0.5

        # Publish the attitude setpoint.
        self.attitude_pub.publish(setpoint)

        # Update previous errors and time for the next loop.
        self.prev_error_x = error_x
        self.prev_error_y = error_y
        self.prev_time = current_time

def main(args=None):
    rclpy.init(args=args)
    node = DroneControlEulerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
