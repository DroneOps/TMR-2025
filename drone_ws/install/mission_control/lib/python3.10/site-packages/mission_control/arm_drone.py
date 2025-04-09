import rclpy
from rclpy.node import Node
from mavros_msgs.srv import SetMode, CommandBool
from mavros_msgs.msg import State
from std_msgs.msg import String
import signal
import sys

class arm_drone(Node):
    def __init__(self):
        super().__init__('arm_drone')

        self.mode_client = self.create_client(SetMode, '/mavros/set_mode')
        self.arm_client = self.create_client(CommandBool, '/mavros/cmd/arming')
        self.state_sub = self.create_subscription(State, '/mavros/state', self.state_cb, 10)
        self.current_state = None
        self.prev_armed_drone_signal = None
        self.armed_drone_signal = False

        self.publisher = self.create_publisher(String, '/armedDrone', 10)

        self.timer = self.create_timer(1.0, self.publish_armed_status_continuously)

        # Handle shutdown gracefully
        signal.signal(signal.SIGINT, self.shutdown_hook)

        # Wait for service availability
        self.wait_for_services()

        # Wait for MAVROS connection
        while rclpy.ok() and (self.current_state is None or not self.current_state.connected):
            self.get_logger().info('⏳ Esperando conexión a MAVROS...')
            rclpy.spin_once(self, timeout_sec=0.5)

        self.get_logger().info("✅ ¡Conectado a MAVROS!")

        self.set_mode()
        self.arm()

    def wait_for_services(self):
        self.get_logger().info('🔄 Esperando servicios de MAVROS...')
        while not self.mode_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('⏳ Servicio /mavros/set_mode no disponible...')
        while not self.arm_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn('⏳ Servicio /mavros/cmd/arming no disponible...')

    def state_cb(self, msg):
        self.current_state = msg
        self.armed_drone_signal = msg.armed

    def set_mode(self):
        request = SetMode.Request()
        request.custom_mode = 'GUIDED_NOGPS'
        future = self.mode_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() and future.result().mode_sent:
            self.get_logger().info("✅ Modo GUIDED_NO_GPS establecido")
        else:
            self.get_logger().error("❌ Error al establecer el modo")

    def arm(self):
        request = CommandBool.Request()
        request.value = True
        future = self.arm_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() and future.result().success:
            self.get_logger().info("✅ ¡Dron armado!")
            self.publish_armed_status("armed")
        else:
            self.get_logger().error("❌ Fallo al armar")

    def disarm(self):
        request = CommandBool.Request()
        request.value = False
        future = self.arm_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() and future.result().success:
            self.get_logger().info("✅ ¡Dron desarmado!")
            self.publish_armed_status("disarmed")
        else:
            self.get_logger().error("❌ Fallo al desarmar")

    def publish_armed_status(self, status: str = None):
        if status is None:
            status = "armed" if self.armed_drone_signal else "disarmed"
        
        msg = String()
        msg.data = status
        self.publisher.publish(msg)
        self.get_logger().info(f"📤 Publicado estado: {status}")
        
    def publish_armed_status_continuously(self):
        current_status = "armed" if self.armed_drone_signal else "disarmed"
        if current_status != self.prev_armed_drone_signal:
            self.prev_armed_drone_signal = current_status
            self.publish_armed_status(current_status)
        else:
            self.get_logger().info("🔄 Estado del dron no ha cambiado.")

    def shutdown_hook(self, signum, frame):
        self.get_logger().info("🛑 Interrupción detectada. Desarmando el dron...")
        self.disarm()
        self.destroy_node()
        rclpy.shutdown()
        sys.exit(0)

def main(args=None):
    rclpy.init(args=args)
    node = arm_drone()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

