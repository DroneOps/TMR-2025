import rclpy
from rclpy.node import Node
from mavros_msgs.srv import SetMode, CommandBool
from mavros_msgs.msg import State
from std_msgs.msg import String
import signal
import sys

class ARMDrone(Node):
    def __init__(self):
        super().__init__('ARMControl')

        self.mode_client = self.create_client(SetMode, '/set_mode')
        self.arm_client = self.create_client(CommandBool, '/mavros/arming')
        self.state_sub = self.create_subscription(State, '/state', self.state_cb, 10)
        self.current_state = None

        self.armed_drone_signal = False  # Variable que almacena el estado del armado

        self.publisher = self.create_publisher(String, '/armedDrone', 10)

        # Publicar estado continuamente cada segundo
        self.create_timer(1.0, self.publish_armed_status_continuously)  # Publicar cada 1 segundo
        
        # Manejador de señal para Ctrl+C
        signal.signal(signal.SIGINT, self.shutdown_hook)

        # Espera a que los servicios estén disponibles
        while not self.mode_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio /set_mode...')

        while not self.arm_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio /mavros/arming...')

        # Espera conexión a MAVROS
        while self.current_state is None or not self.current_state.connected:
            self.get_logger().info('Esperando conexión a MAVROS...')
            rclpy.spin_once(self)

        self.get_logger().info("✅ ¡Conectado a MAVROS!")

        self.set_mode()
        self.arm()

    def state_cb(self, msg):
        self.current_state = msg
        # Actualizamos el estado de armado en base a la información de MAVROS
        self.armed_drone_signal = msg.armed

    def set_mode(self):
        request = SetMode.Request()
        request.custom_mode = 'STABILIZE'
        future = self.mode_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() and future.result().mode_sent:
            self.get_logger().info("✅ Modo STABILIZE establecido")
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
        """
        Publica el estado del dron en el topic /armedDrone.
        Si no se pasa el estado como parámetro, lo publica como 'armed' o 'disarmed' basado en el estado actual.
        """
        if status is None:
            # Si no se pasa un estado, publicamos el estado actual del dron
            status = "armed" if self.armed_drone_signal else "disarmed"
        
        msg = String()
        msg.data = status
        self.publisher.publish(msg)
        self.get_logger().info(f"📤 Publicado estado: {status}")
    
    def publish_armed_status_continuously(self):
        """
        Publica el estado del dron cada segundo.
        """
        self.publish_armed_status()

    def shutdown_hook(self, signum, frame):
        self.get_logger().info("🛑 Interrupción detectada. Desarmando el dron...")
        self.disarm()
        self.destroy_node()
        rclpy.shutdown()
        sys.exit(0)

def main(args=None):
    rclpy.init(args=args)
    node = ARMDrone()
    # Mantiene el nodo vivo y publicando mensajes
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
