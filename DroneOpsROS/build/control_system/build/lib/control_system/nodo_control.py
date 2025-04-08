import rclpy
from rclpy.node import Node
from mavros_msgs.srv import SetMode, CommandBool
from mavros_msgs.msg import State
import signal


class DroneControl(Node):
    def __init__(self):
        super().__init__('DroneControl')

        self.mode_client = self.create_client(SetMode, '/set_mode')
        self.arm_client = self.create_client(CommandBool, '/mavros/arming')
        self.state_sub = self.create_subscription(State, '/state', self.state_cb, 10)
        self.current_state = None

        while not self.mode_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /set_mode service...')

        while not self.arm_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /cmd/arming service...')

        # Aquí, estamos esperando que la conexión esté lista antes de proceder
        while self.current_state is None or not self.current_state.connected:
            self.get_logger().info('Esperando conexión a MAVROS...')
            rclpy.spin_once(self)

        # Una vez que la conexión esté lista, ahora puedes configurar el modo y armar el dron
        self.get_logger().info("¡Conectado a MAVROS!")
        self.set_mode()  # Establece el modo del dron
        self.arm()  # Arma el dron

        signal.signal(signal.SIGINT, self.shutdown_hook)
    def state_cb(self, msg):
        # Aquí se actualiza el estado actual
        self.current_state = msg

    def set_mode(self):
        request = SetMode.Request()
        request.custom_mode = 'STABILIZE'  # Modo deseado
        future = self.mode_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.get_logger().info(f"Mode set result: {future.result()}")

        if future.result() is not None and future.result().mode_sent:
            self.get_logger().info("Modo STABILIZE🚁")
        else:
            self.get_logger().error("NO se pudo establecer el modo🚁❌ ")

    def arm(self):
        request = CommandBool.Request()
        request.value = True
        future = self.arm_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.get_logger().info(f"Arming result: {future.result()}")

        if future.result().success:
            self.get_logger().info("✅ ¡Dron armado!")
        else:
            self.get_logger().error("❌ Fallo al armar")


    def disarm(self):
        # Desarmar el dron
        request = CommandBool.Request()
        request.value = False
        future = self.arm_client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        self.get_logger().info(f"Disarming result: {future.result()}")

        if future.result().success:
            self.get_logger().info("✅ ¡Dron desarmado!")
        else:
            self.get_logger().error("❌ Fallo al desarmar")

    def shutdown_hook(self, signum, frame):
        # Llamar a la función de desarme antes de cerrar el nodo
        self.get_logger().info("Cerrando el programa, desarmando el dron...")
        self.disarm()  # Desarma el dron antes de finalizar
        self.destroy_node()  # Destruye el nodo de ROS
        rclpy.shutdown()  # Finaliza ROS

def main(args=None):
    rclpy.init(args=args)
    node = DroneControl()  # Llama a la clase de control que maneja todo
    rclpy.spin(node)  # Espera mientras el nodo está activo
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
