import rclpy
from rclpy.node import Node
import math
from std_msgs.msg import Float64
from geometry_msgs.msg import Point
from sensor_msgs.msg import Imu
from message_filters import Subscriber, ApproximateTimeSynchronizer
from mavros_msgs.msg import AttitudeTarget
from aruco_drone_control.aruco_drone_control.pid_controller_node import DroneControlEulerNode

class TakeoffControl(Node):
    def __init__(self):
        super().__init__('takeoff_control')
        self.target_altitude = 2.0  # Target takeoff altitude in meters
        self.throttle = 0.0
        self.current_altitude = 0.0
        self.marker_x = None
        self.marker_y = None
        self.current_yaw = 0.0

        # Subscribers for altitude and IMU
        self.current_altitude_subscriber = self.create_subscription(
            Float64,

            '/mavros/global_position/rel_alt',
            self.altitude_callback,
            10
        )

        # Subscribers for marker position and IMU using message filters
        self.marker_sub = Subscriber(self, Point, '/marker_position')
        self.imu_sub = Subscriber(self, Imu, '/imu')

        # Synchronize marker and IMU data
        self.ts = ApproximateTimeSynchronizer([self.marker_sub, self.imu_sub], queue_size=10, slop=0.1)
        self.ts.registerCallback(self.synchronized_callback)

        # Publisher for AttitudeTarget
        self.attitude_pub = self.create_publisher(
            AttitudeTarget,
            '/mavros/setpoint_raw/attitude',
            10
        )

        # Initialize DroneControlEulerNode for PID control
        self.pid_controller = DroneControlEulerNode()

        # Timer to manage takeoff and stabilization
        self.create_timer(1.0, self.control_takeoff_and_stabilize)

    def altitude_callback(self, msg):
        # Update current altitude
        self.current_altitude = msg.data
        self.get_logger().info(f"Current altitude: {self.current_altitude} m")

    def synchronized_callback(self, marker_msg, imu_msg):
        # Synchronize and process marker and IMU data
        self.marker_x = marker_msg.x
        self.marker_y = marker_msg.y
        self.get_logger().info(f"Marker position: X={self.marker_x}, Y={self.marker_y}")

        # Extract yaw from IMU data
        q = imu_msg.orientation
        siny_cosp = 2 * (q.w * q.z + q.x * q.y)
        cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
        self.current_yaw = math.atan2(siny_cosp, cosy_cosp)
        self.get_logger().info(f"Yaw: {math.degrees(self.current_yaw):.2f}°")

    def control_takeoff_and_stabilize(self):
        if self.current_altitude < self.target_altitude:
            # Increase throttle until target altitude is reached
            self.throttle = min(self.throttle + 0.05, 1.0)
            self.send_takeoff_command(self.throttle)
            self.get_logger().info(f"Takeoff in progress: Altitude: {self.current_altitude} m, Throttle: {self.throttle}")
        else:
            # Once altitude is reached, stabilize the drone over the marker
            self.stabilize_over_marker()
            self.get_logger().info("Takeoff completed! Stabilizing over marker.")

    def stabilize_over_marker(self):
        if self.marker_x is None or self.marker_y is None:
            self.get_logger().warn("No marker data received.")
            return

        # Call the PID control method to stabilize over the marker
        self.pid_controller.marker_x = self.marker_x
        self.pid_controller.marker_y = self.marker_y

        # Run the PID control loop
        self.pid_controller.control_loop()

        # Maintain altitude with the same throttle
        setpoint = AttitudeTarget()
        setpoint.header.stamp = self.get_clock().now().to_msg()
        setpoint.type_mask = 7  # Ignore body rates
        setpoint.orientation = self.pid_controller.attitude_pub
        setpoint.thrust = self.throttle  # Keep the throttle constant

        self.attitude_pub.publish(setpoint)

    def send_takeoff_command(self, throttle):
        # Send throttle command to the Pixhawk or controller
        pass

def main(args=None):
    rclpy.init(args=args)
    node = TakeoffControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
