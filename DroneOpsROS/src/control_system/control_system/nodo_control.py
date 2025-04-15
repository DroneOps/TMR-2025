#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import math
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Quaternion, PoseStamped
from mavros_msgs.msg import AttitudeTarget
from std_msgs.msg import Int32MultiArray
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

def clamp(val, low, high):
    return max(low, min(high, val))

def euler_to_quaternion(roll, pitch, yaw):
    # Convert Euler angles (in radians) to quaternion.
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

class DroneControlFullNode(Node):
    def __init__(self):
        super().__init__('drone_control_full_node')

        # -------- Controller Parameters --------
        # Altitude control
        self.declare_parameters(namespace='', parameters=[
            ('kp_z', 0.1), ('ki_z', 0.01), ('kd_z', 0.1),
            ('desired_altitude', 1.10), ('mass', 1.6),
            ('max_thrust', 31.0), ('gravity', 9.81)
        ])

        # Attitude control (for fine tuning pitch and roll)
        self.declare_parameters(namespace='', parameters=[
            ('kp_pitch', 0.8), ('ki_pitch', 0.0), ('kd_pitch', 0.1),
            ('kp_roll', 0.8), ('ki_roll', 0.0), ('kd_roll', 0.1)
        ])

        # Lateral control (marker based)
        self.declare_parameters(namespace='', parameters=[
            ('kp', 0.0005), ('ki', 0.0), ('kd', 0.5),
            ('desired_x', 0.0), ('desired_y', 0.0),
            ('thrust_nominal', 15.0)
        ])

        # Load all parameters
        self.load_parameters()

        # -------- Controller State --------
        self.init_controller_state()
        self.current_yaw = 0.0
        self.marker_x = None
        self.marker_y = None

        # -------- Subscribers & Publishers --------
        self.init_subscriptions()
        self.attitude_pub = self.create_publisher(AttitudeTarget, '/mavros/setpoint_raw/attitude', 10)
        self.timer = self.create_timer(0.1, self.control_loop)

    def load_parameters(self):
        # Altitude control
        self.kp_z = self.get_parameter('kp_z').value
        self.ki_z = self.get_parameter('ki_z').value
        self.kd_z = self.get_parameter('kd_z').value
        self.desired_altitude = self.get_parameter('desired_altitude').value
        self.mass = self.get_parameter('mass').value
        self.max_thrust = self.get_parameter('max_thrust').value
        self.gravity = self.get_parameter('gravity').value

        # Attitude control
        self.kp_pitch = self.get_parameter('kp_pitch').value
        self.ki_pitch = self.get_parameter('ki_pitch').value
        self.kd_pitch = self.get_parameter('kd_pitch').value
        self.kp_roll = self.get_parameter('kp_roll').value
        self.ki_roll = self.get_parameter('ki_roll').value
        self.kd_roll = self.get_parameter('kd_roll').value

        # Lateral control
        self.kp = self.get_parameter('kp').value
        self.ki = self.get_parameter('ki').value
        self.kd = self.get_parameter('kd').value
        self.desired_x = self.get_parameter('desired_x').value
        self.desired_y = self.get_parameter('desired_y').value
        self.thrust_nominal = self.get_parameter('thrust_nominal').value

    def init_controller_state(self):
        # PID states
        self.integral_z = 0.0
        self.prev_error_z = 0.0
        self.integral_pitch = 0.0
        self.prev_error_pitch = 0.0
        self.integral_roll = 0.0
        self.prev_error_roll = 0.0
        self.integral_x = 0.0
        self.integral_y = 0.0
        self.prev_error_x = 0.0
        self.prev_error_y = 0.0
        self.prev_time = self.get_clock().now().nanoseconds / 1e9

        # State variables
        self.current_altitude = 0.0
        self.current_roll = 0.0
        self.current_pitch = 0.0

    def init_subscriptions(self):
        # IMU subscription
        self.imu_sub = self.create_subscription(Imu, '/imu', self.imu_callback, 10)
        
        # Altitude subscription
        qos_alt = QoSProfile(
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST,
            depth=10
        )
        self.alt_sub = self.create_subscription(PoseStamped, '/mavros/local_position/pose', self.altitude_callback, qos_alt)

        # Marker subscription
        self.marker_sub = self.create_subscription(Int32MultiArray, '/marker_info', self.marker_callback, 10)

    def imu_callback(self, msg: Imu):
        q = msg.orientation
        # Roll calculation
        sinr_cosp = 2 * (q.w * q.x + q.y * q.z)
        cosr_cosp = 1 - 2 * (q.x * q.x + q.y * q.y)
        self.current_roll = math.atan2(sinr_cosp, cosr_cosp)

        # Pitch calculation with clamping
        sinp = 2 * (q.w * q.y - q.z * q.x)
        self.current_pitch = math.asin(clamp(sinp, -1.0, 1.0))

        # Yaw calculation
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        self.current_yaw = math.atan2(siny_cosp, cosy_cosp)

    def altitude_callback(self, msg: PoseStamped):
        self.current_altitude = msg.pose.position.z

    def marker_callback(self, msg: Int32MultiArray):
        if len(msg.data) >= 3:
            self.marker_x = float(msg.data[1])
            self.marker_y = float(msg.data[2])
        else:
            self.marker_x = None
            self.marker_y = None

    def control_loop(self):
        current_time = self.get_clock().now().nanoseconds / 1e9
        dt = current_time - self.prev_time
        if dt <= 0:
            dt = 0.1

        # -------- Altitude Control --------
        error_z = self.desired_altitude - self.current_altitude
        self.integral_z += error_z * dt
        derivative_z = (error_z - self.prev_error_z) / dt

        tilt_compensation = math.cos(self.current_roll) * math.cos(self.current_pitch)
        thrust_base = (self.mass * self.gravity) / (self.max_thrust * tilt_compensation)
        thrust_pid = self.kp_z * error_z + self.ki_z * self.integral_z + self.kd_z * derivative_z
        computed_thrust = clamp(thrust_base + thrust_pid, 0.0, 1.0)

        # -------- Lateral Control --------
        theta_c, phi_c = 0.0, 0.0
        if self.marker_x is not None and self.marker_y is not None:
            error_x = self.marker_x - self.desired_x
            error_y = self.marker_y - self.desired_y

            # X-axis control to command desired pitch (theta_c)
            self.integral_x += error_x * dt
            derivative_x = (error_x - self.prev_error_x) / dt
            control_x = self.kp * error_x + self.ki * self.integral_x + self.kd * derivative_x
            theta_c = math.asin(clamp(control_x * self.mass / self.thrust_nominal, -1.0, 1.0))

            # Y-axis control to command desired roll (phi_c)
            self.integral_y += error_y * dt
            derivative_y = (error_y - self.prev_error_y) / dt
            control_y = self.kp * error_y + self.ki * self.integral_y + self.kd * derivative_y
            # FIXED: Corrected the misplaced parenthesis in the clamp call.
            phi_c = math.asin(clamp(-control_y * self.mass / (math.cos(theta_c) * self.thrust_nominal), -1.0, 1.0))

            self.prev_error_x = error_x
            self.prev_error_y = error_y

        # -------- Attitude Control --------
        # Compute desired corrections (PID refinement for pitch and roll)
        error_pitch = theta_c - self.current_pitch
        self.integral_pitch += error_pitch * dt
        derivative_pitch = (error_pitch - self.prev_error_pitch) / dt
        pid_pitch = self.kp_pitch * error_pitch + self.ki_pitch * self.integral_pitch + self.kd_pitch * derivative_pitch

        error_roll = phi_c - self.current_roll
        self.integral_roll += error_roll * dt
        derivative_roll = (error_roll - self.prev_error_roll) / dt
        pid_roll = self.kp_roll * error_roll + self.ki_roll * self.integral_roll + self.kd_roll * derivative_roll

        # -------- Command Generation --------
        setpoint = AttitudeTarget()
        setpoint.header.stamp = self.get_clock().now().to_msg()
        setpoint.type_mask = 7  # Ignore angular rates
        # Command the drone using the refined attitude commands
        setpoint.orientation = euler_to_quaternion(pid_roll, pid_pitch, self.current_yaw)
        setpoint.thrust = computed_thrust

        self.attitude_pub.publish(setpoint)

        # -------- State Update --------
        self.prev_error_z = error_z
        self.prev_error_pitch = error_pitch
        self.prev_error_roll = error_roll
        self.prev_time = current_time

        # -------- Logging --------
        self.get_logger().info(
            f"Alt: {self.current_altitude:.2f}m | "
            f"Pitch: {math.degrees(self.current_pitch):.1f}°→{math.degrees(theta_c):.1f}° | "
            f"Roll: {math.degrees(self.current_roll):.1f}°→{math.degrees(phi_c):.1f}° | "
            f"Thrust: {computed_thrust:.2f}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = DroneControlFullNode()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

