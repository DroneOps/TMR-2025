#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import math
from sensor_msgs.msg import Imu
from geometry_msgs.msg import PoseStamped
from mavros_msgs.msg import AttitudeTarget
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

def clamp(val, low, high):
    return max(low, min(high, val))

class AltitudeControl(Node):
    def __init__(self):
        super().__init__('altitude_control')

        self.declare_parameters(namespace='', parameters=[
            ('kp_z', 0.1),
            ('ki_z', 0.00006),
            ('kd_z', 0.15),
            ('mass', 1.6),
            ('max_thrust', 31),
            ('gravity', 9.81),
            ('hold_time', 5.0)  # Hold at target height before descending
        ])

        # Params
        self.kp_z = self.get_parameter('kp_z').value
        self.ki_z = self.get_parameter('ki_z').value
        self.kd_z = self.get_parameter('kd_z').value
        self.mass = self.get_parameter('mass').value
        self.max_thrust = self.get_parameter('max_thrust').value
        self.gravity = self.get_parameter('gravity').value
        self.hold_time = self.get_parameter('hold_time').value

        # States
        self.integral_z = 0.0
        self.prev_error_z = 0.0
        self.prev_time = self.get_clock().now().nanoseconds / 1e9
        self.current_altitude = 0.0
        self.current_roll = 0.0
        self.current_pitch = 0.0

        # State machine vars
        self.state = 'ASCEND'
        self.target_altitude = 1.5
        self.hold_start_time = None

        # Subscribers
        self.create_subscription(Imu, '/imu', self.imu_callback, 10)

        qos_alt = QoSProfile(
            depth=10,
            reliability=QoSReliabilityPolicy.BEST_EFFORT,
            history=QoSHistoryPolicy.KEEP_LAST
        )
        self.create_subscription(PoseStamped, '/mavros/local_position/pose', self.altitude_callback, qos_alt)

        # Publisher
        self.attitude_pub = self.create_publisher(
            AttitudeTarget, '/mavros/setpoint_raw/attitude', 10)

        self.timer = self.create_timer(0.1, self.control_loop)
        self.get_logger().info("Altitude control node started")

    def imu_callback(self, msg: Imu):
        q = msg.orientation
        sinp = 2 * (q.w * q.y - q.z * q.x)
        self.current_pitch = math.asin(clamp(sinp, -1.0, 1.0))

        sinr_cosp = 2 * (q.w * q.x + q.y * q.z)
        cosr_cosp = 1 - 2 * (q.x * q.x + q.y * q.y)
        self.current_roll = math.atan2(sinr_cosp, cosr_cosp)

    def altitude_callback(self, msg: PoseStamped):
        self.current_altitude = msg.pose.position.z

    def control_loop(self):
        current_time = self.get_clock().now().nanoseconds / 1e9
        dt = current_time - self.prev_time
        if dt <= 0:
            dt = 0.1

               # Transition logic
        if self.state == 'ASCEND':
            self.target_altitude = 1.5
            if self.current_altitude >= 1.4:
                self.state = 'HOLD'
                self.hold_start_time = current_time
                self.get_logger().info("Reached target altitude. Holding...")

        elif self.state == 'HOLD':
            if current_time - self.hold_start_time > self.hold_time:
                self.state = 'DESCEND'
                self.get_logger().info("Hold complete. Descending...")

        elif self.state == 'DESCEND':
            self.target_altitude = -2.0  # More negative to force descent
            if self.current_altitude <= 0.25:  # Slightly more lenient threshold
                self.state = 'LAND'
                self.get_logger().info("Landed.")

        elif self.state == 'LAND':
            # Optional: kill thrust completely after landing
            setpoint = AttitudeTarget()
            setpoint.header.stamp = self.get_clock().now().to_msg()
            setpoint.type_mask = 7
            setpoint.thrust = 0.0
            self.attitude_pub.publish(setpoint)
            self.get_logger().info("Thrust set to 0.")
            return


        # PID Control
        error_z = self.target_altitude - self.current_altitude
        self.integral_z += error_z * dt
        derivative_z = (error_z - self.prev_error_z) / dt

        tilt_comp = math.cos(self.current_roll) * math.cos(self.current_pitch)
        thrust_base = (self.mass * self.gravity) / (self.max_thrust * tilt_comp)
        thrust_pid = self.kp_z * error_z + self.ki_z * self.integral_z + self.kd_z * derivative_z
        thrust = clamp(thrust_base + thrust_pid, 0.0, 1.0)

        setpoint = AttitudeTarget()
        setpoint.header.stamp = self.get_clock().now().to_msg()
        setpoint.type_mask = 7
        setpoint.thrust = thrust
        self.attitude_pub.publish(setpoint)

        # Update
        self.prev_error_z = error_z
        self.prev_time = current_time

        self.get_logger().info(
            f"State: {self.state} | Target: {self.target_altitude:.2f}m | Current: {self.current_altitude:.2f}m | Thrust: {thrust:.2f}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = AltitudeControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

