#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy
from geometry_msgs.msg import Quaternion, PoseStamped
from mavros_msgs.msg import AttitudeTarget

class ArucoControl(Node):
    def __init__(self):
        super().__init__('aruco_control')

        # Parámetros PID_z
        self.desired_altitude = 1.0
        self.current_altitude = 0.0

        self.Kp_z = 0.4
        self.Ki_z = 0.1
        self.Kd_z = 0.05
        
        initial_error = self.desired_altitude - self.current_altitude
        self.prev_error_z = initial_error

        # Estados internos
        self.current_altitude = 0.0
        self.integral_z       = 0.0
        self.dt               = 0.1  # Periodo del timer

        # Subscripción a la pose (para leer z)
        qos = QoSProfile(depth=10,
                         reliability=QoSReliabilityPolicy.BEST_EFFORT,
                         history=QoSHistoryPolicy.KEEP_LAST)
        self.create_subscription(PoseStamped,
                                 '/mavros/local_position/pose',
                                 self.altitude_callback,
                                 qos)

        # Publicador de thrust
        self.thrust_pub = self.create_publisher(
            AttitudeTarget,
            '/mavros/setpoint_raw/attitude',
            10)

        # Timer al loop de control
        self.create_timer(self.dt, self.control_loop)

    def altitude_callback(self, msg: PoseStamped):
        self.current_altitude = msg.pose.position.z

    def control_loop(self):
        error_z = self.desired_altitude - self.current_altitude

        # Integral con anti‐windup
        self.integral_z += error_z * self.dt
        # Limita la integral para que no crezca sin control
        max_int = 1.0 / (self.Ki_z + 1e-9)
        self.integral_z = max(min(self.integral_z, max_int), -max_int)

        # Derivativo
        derivative_z = (error_z - self.prev_error_z) / self.dt

        # PID
        thrust = (
            self.Kp_z * error_z +
            self.Ki_z * self.integral_z +
            self.Kd_z * derivative_z
        )

        # Clamp entre 0 y 1
        thrust = max(0.0, min(1.0, thrust))

        # Guarda para la siguiente iteración
        self.prev_error_z = error_z

        # Publica el comando
        msg = AttitudeTarget()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.type_mask = 1 | 2 | 4 | 128   #ignora todo menos thrust
        msg.orientation = Quaternion(x=0.0, y=0.0, z=0.0, w=1.0)
        msg.thrust = float(thrust)
        self.thrust_pub.publish(msg)

        # Log
        self.get_logger().info(
            f'Alt: {self.current_altitude:.2f}  Err: {error_z:.2f}  '
            f'I: {self.integral_z:.2f}  D: {derivative_z:.2f}  '
            f'Thr: {thrust:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = ArucoControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
