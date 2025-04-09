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

        self.mode_client = self.create_client(SetMode, '/set_mode')
        self.arm_client = self.create_client(CommandBool, '/mavros/arming')
        self.state_sub = self.create_subscription(State, '/state', self.state_cb, 10)
        self.current_state = None

        #para manejo de si se detecat un cambio 
        self.armed_drone_signal = False  
        self.prev_armed_drone_signal = None

        self.publisher = self.create_publisher(String, '/armed_drone', 10)

        # Publicar estado continuamente cada segundo
        self.create_timer(1.0, self.publish_armed_status_continuously)  # Publicar cada 1 segundo

        # Manejador de señal para Ctrl+C
        signal.signal(signal.SIGINT, self.shutdown_hook)

         # Espera a que los servicios estén disponibles
        while self.current_state is None or not self.current_state.connected: #mavros
            self.get_logger().info('Esperando conexión a MAVROS...')
            rclpy.spin_once(self)
            self.get_logger().info("✅ ¡Conectado a MAVROS!")
       
        while not self.mode_client.wait_for_service(timeout_sec=1.0):#espera al servicio de modo
            self.get_logger().info('Esperando servicio /set_mode...')

        while not self.arm_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Esperando servicio /mavros/arming...')
        

        #iniciar aqui para que siempre se este mandando los mensajes 
        self.set_mode()
        self.arm()


    def state_cb(self, msg):
        self.current_state = msg
        self.armed_drone_signal = msg.armed

    def set_mode(self):
        request = SetMode.Request()
        request.custom_mode = 'GUIDED_NOGPS'
        future = self.mode_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() and future.result().mode_sent:
            self.get_logger().info("✅ Modo GUIDED_NOGPS establecido")
        else:
            self.get_logger().error("❌ Error al establecer el modo")

    def arm(self):
        request = CommandBool.Request()
        request.value = True
        future = self.arm_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() and future.result().success:
            self.get_logger().info("✅ ¡Dron armado!")
            self.armed_drone_signal = True
        else:
            self.get_logger().error("❌ Fallo al armar")

    def disarm(self):
        request = CommandBool.Request()
        request.value = False
        future = self.arm_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        if future.result() and future.result().success:
            self.get_logger().info("✅ ¡Dron desarmado!")
            self.armed_drone_signal = False
        else:
            self.get_logger().error("❌ Fallo al desarmar")

    def publish_armed_status(self, status):
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
