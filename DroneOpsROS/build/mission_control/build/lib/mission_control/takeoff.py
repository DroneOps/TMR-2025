import rclpy
from rclpy.node import Node
import math
from std_msgs.msg import Float64, String
from sensor_msgs.msg import Range, Imu
from geometry_msgs.msg import Point, Quaternion
from message_filters import Subscriber, ApproximateTimeSynchronizer
from mavros_msgs.msg import AttitudeTarget
from pymavlink import mavutil
import time

class TakeoffControl(Node):
    def __init__(self):
        super().__init__('TakeoffControl')
        self.target_altitude = None  # Altitud objetivo para despegue en metros
        self.throttle = 0.0
        self.current_altitude = 0.0  # Añadido para evitar atributo no definido

        # Suscripción al nodo del rangefinder
        self.current_altitude_subscriber = self.create_subscription(
            Range,
            '/mavros/rangefinder/rangefinder',
            self.altitude_callback,
            10
        )

        # Publisher para enviar la actitud con thrust (usando MAVROS)
        self.attitude_pub = self.create_publisher(
            AttitudeTarget,
            '/mavros/setpoint_raw/attitude',
            10
        )

        self.publisher_takeoff = self.create_publisher(String, '/takeoff_drone', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        # Se crea y publica un mensaje AttitudeTarget que establece una actitud neutra y thrust=0.7
        att_msg = AttitudeTarget()
        att_msg.header.stamp = self.get_clock().now().to_msg()
        att_msg.type_mask = 7  # Ignora los campos de body_rate
        # Se define la orientación neutra con un cuaternión; 
        # nota: el cuaternión identidad es (x=0, y=0, z=0, w=1) pero se puede usar (1,0,0,0) si ya se ha comprobado que funciona en tu sistema.
        att_msg.orientation = Quaternion(x=1.0, y=0.0, z=0.0, w=0.0)
        att_msg.thrust = 0.7  # 70% de empuje

        self.attitude_pub.publish(att_msg)
        self.get_logger().info("Enviando AttitudeTarget con thrust 0.7")

    def altitude_callback(self, msg):
        # Actualiza la altitud actual
        self.current_altitude = msg.range
        self.get_logger().info(f"Altitud Actual: {self.current_altitude} m")

    def set_altitude(self, target_altitude):
        self.target_altitude = target_altitude

    def publisherTakeoff(self, take_off):
        msg = String()
        msg.data = take_off
        self.publisher_takeoff.publish(msg)
        

def main(args=None):
    rclpy.init(args=args)
    node = TakeoffControl()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()