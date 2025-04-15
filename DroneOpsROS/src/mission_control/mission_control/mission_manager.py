#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from mavros_msgs.msg import State
from std_msgs.msg import Float64
from rclpy.qos import QoSProfile
from rclpy.qos import QoSDurabilityPolicy, QoSReliabilityPolicy
from rclpy.qos import QoSHistoryPolicy
from mission_control.srv import Altitud
from std_msgs.msg import Int32MultiArray


class mission_manager(Node): 
    def __init__(self):
        super().__init__('mission_manager') 
        self.armed_drone_signal = False
        self.state = "Disarmed" 

        #suscripciones
        self.armado = self.create_subscription(String, '/armed_drone', self.armed_callback, 10)
        self.marker_sub = self.create_subscription(Int32MultiArray,'/marker_info',self.marker_callback,10)

        self.create_timer(1.0, self.control_loop)  # Loop de control de misión, se ejecuta cada segundo
        
        # clientes a los servicios
        self.cli_takeoff = self.create_client(Altitud, 'takeoff_drone' )

        # Publicador para manejar el cambio de tareas
        self.task_publisher = self.create_publisher(String, '/current_task', 10)
        
        self.get_logger().info("Mission Empezada")


    def armed_callback(self, msg):
        self.get_logger().info(f"📩 Recibido mensaje de armado: {msg.data}")
        self.armed_status = msg.data

        if msg.data == "armed":
            self.armed_drone_signal = True
        elif msg.data == "disarmed":
            self.armed_drone_signal = False

    def marker_callback(self, msg):
        if msg.data:  # Verifica que no esté vacío
            self.id_aruco = msg.data[0]
            self.get_logger().info(f'id del aruco detectado: {self.id_aruco}')
    
    def control_loop(self):
        if self.state == "Disarmed" or self.armed_drone_signal == False:
            self.state = "init"
            self.publish_task("init")
    
        # Pasar a esperar comando de takeoff
        elif self.state == "init" and self.id_aruco == 100:
            self.state = "takeoff"
            self.publish_task("takeoff")
    
        # takeoff y llamamamos al takeoff con la altitud que queremos
        elif self.state == "takeoff":
            if not self.cli_takeoff.wait_for_service(timeout_sec=1.0):
                self.get_logger().info('⏳ Esperando servicio de despegue...')
                return

            req = Altitud.Request()
            req.altitud = 1.5  # desired altitude in meters

            future = self.cli_takeoff.call_async(req)
            rclpy.spin_until_future_complete(self, future)

            if future.result() is not None:
                self.get_logger().info(
                    f"🛫 Despegue iniciado, altitud recibida: {future.result().response_altitud} m")
                self.state = "takeoff_complete"
                self.publish_task("takeoff_complete")
            else:
                self.get_logger().error("❌ Error al llamar al servicio de despegue")
    

        elif self.state == "takeoff_complete":
            self.state = "aruco_nav"
            self.publish_task("aruco_nav")

        elif self.state == "aruco_nav":
            self.state = "line_follow"
            self.publish_task("line_follow")
    

        elif self.state == "line_follow":
            self.state = "final_task"
            self.publish_task("final_task")
    

        elif self.state == "final_task":
            self.state = "mission_complete"
            self.publish_task("mission_complete")


    def publish_task(self, task_name: str):
        """
        Publica el nombre de la tarea actual en el topic `/current_task`.
        """
        msg = String()
        msg.data = task_name
        self.task_publisher.publish(msg)
        self.get_logger().info(f"Task {task_name} initiated")


def main(args=None):
    rclpy.init(args=args)
    node = mission_manager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()