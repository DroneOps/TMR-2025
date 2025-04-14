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


class mission_manager(Node): 
    def __init__(self):
        super().__init__('mission_manager') 
        self.armed_drone_signal = False
        self.state = "Disarmed"  
        self.armado = self.create_subscription(String, '/armed_drone', self.armed_callback, 10)
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

    
    def control_loop(self):
        """
        This loop checks and updates the mission state every second.
        """
        # Transition from "Disarmed" to "init" only once.
        if self.state == "Disarmed" and self.armed_drone_signal:
            self.state = "init"
            self.publish_task("init")
    
        # Transition from "init" to "takeoff"
        elif self.state == "init":
            self.state = "takeoff"
            self.publish_task("takeoff")
    
        # In the "takeoff" state, we call the takeoff service.
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
    
        # Transition from "takeoff_complete" to "aruco_nav"
        elif self.state == "takeoff_complete":
            self.state = "aruco_nav"
            self.publish_task("aruco_nav")
    
        # Transition from "aruco_nav" to "line_follow" (placeholder)
        elif self.state == "aruco_nav":
            self.state = "line_follow"
            self.publish_task("line_follow")
    
        # Transition from "line_follow" to "final_task" (placeholder)
        elif self.state == "line_follow":
            self.state = "final_task"
            self.publish_task("final_task")
    
        # Transition from "final_task" to "mission_complete"
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
