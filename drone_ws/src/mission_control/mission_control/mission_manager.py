import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from mavros_msgs.msg import State
from std_msgs.msg import Float64
from rclpy.qos import QoSProfile
from rclpy.qos import QoSDurabilityPolicy, QoSReliabilityPolicy
from rclpy.qos import QoSHistoryPolicy



class mission_manager(Node): 
    def __init__(self):
        super().__init__('mission_manager')
        self.target_altitude = 1.0  # Altura objetivo de despegue
        self.throttle = 0.0  # Inicializamos el throttle en 0
        self.armed_drone_signal = False
        self.state = "Disarmed"  

        self.armado = self.create_subscription(String, '/armedDrone', self.armed_callback, 10)

        # QoS for MAVROS sensor data
        qos_profile = QoSProfile(depth=10)
        qos_profile.reliability = QoSReliabilityPolicy.BEST_EFFORT

        
        self.current_altitude = self.create_subscription(
            Float64,
            '/mavros/global_position/rel_alt',
            self.altitude_callback,
            qos_profile
        )

        self.create_timer(1.0, self.control_loop)  # Loop de control de misión

        # Publicador para manejar el cambio de tareas
        self.task_publisher = self.create_publisher(String, '/current_task', 10)
        
        self.get_logger().info("Mission Control Node Initialized")


    def armed_callback(self, msg):
        self.get_logger().info(f"📩 Recibido mensaje de armado: {msg.data}")
        self.armed_status = msg.data

        if msg.data == "armed":
            self.armed_drone_signal = True
        elif msg.data == "disarmed":
            self.armed_drone_signal = False

    def altitude_callback(self, msg):
    # msg.data is a Float64 representing the altitude (in meters)
        self.current_altitude_value = msg.data
        self.get_logger().info(f"Altitud recibida: {self.current_altitude_value} m")

    
    def control_loop(self):
        """
        Este loop controla las misiones y cambia entre tareas.
        """
        if self.state == "Disarmed" and self.armed_drone_signal:
            self.state = "init"
            self.publish_task("init")
            

        if self.state == "init":
            self.state = "takeoff"
            self.publish_task("takeoff")
        
        elif self.state == "takeoff":
            # Aquí podrías esperar un mensaje de que el dron ha despegado
            self.increase_throttle_until_altitude()  # Aumentar el throttle hasta alcanzar la altitud deseada
            if self.current_altitude >= self.target_altitude:
                self.state = "takeoff_complete"
                self.get_logger().info("¡Despegue completado! Alcanzada la altitud deseada.")
                self.publish_task("takeoff_complete")
        elif self.state == "takeoff_complete":

            self.state = "aruco_nav"
            self.publish_task("aruco_navigation")
        
        elif self.state == "aruco_nav":
            # Llamar a la lógica para navegar hacia el ArUco
            self.state = "line_follow"
            self.publish_task("line_follow")
        
        elif self.state == "line_follow":
            # Llamar a la lógica para seguir la línea
            self.state = "final_task"
            self.publish_task("final_task")
        
        elif self.state == "final_task":
            # Realizar la tarea final (ej. aterrizaje o acción final)
            self.state = "mission_complete"
            self.publish_task("mission_complete")

    def increase_throttle_until_altitude(self):
        """
        Aumenta el throttle progresivamente hasta que el dron alcance la altitud deseada.
        """
        # Incrementar el throttle poco a poco
        if self.current_altitude < self.target_altitude:
            # Aumentar throttle si no hemos alcanzado la altura objetivo
            self.throttle = min(self.throttle + 0.05, 1.0)  # Limitar throttle máximo a 1.0
            # Aquí envías el comando de actitud y throttle a la Pixhawk
            self.send_attitude_target(0, 0, 0, self.throttle)  # Mantener orientación (0, 0, 0) y ajustar el throttle

            # Aquí podrías obtener la altitud actual del dron (a través de telemetría, por ejemplo)
            self.current_altitude = self.get_current_altitude()  # Necesitarás implementar este método

            self.get_logger().info(f"Despegue en progreso: Altitud actual: {self.current_altitude} m, Throttle: {self.throttle}")
        
        if self.current_altitude >= self.target_altitude:
            # Una vez alcanzada la altura deseada, cambiar de estado
            self.state = "takeoff_complete"
            self.get_logger().info("¡Despegue completado! Alcanzada la altitud deseada.")

    def send_attitude_target(self, roll, pitch, yaw, throttle):
        """
        Enviar comando de actitud y throttle a la Pixhawk.
        """
        # Aquí implementas el envío de cuaterniones con el comando adecuado
        # y también envías el valor de throttle para controlar la altitud
        pass

    def get_current_altitude(self):
        """
        Obtener la altitud actual del dron.
        Este es un método simulado, debes implementarlo con la telemetría.
        """
        # Aquí deberías implementar la obtención de la altitud real del dron
        # Por ejemplo, usando MAVROS o cualquier otro método de telemetría.
        return getattr(self, "current_altitude_value", 0.0)

        
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
def control_loop(self):
    """
    Este loop controla las misiones y cambia entre tareas.
    """
    if self.state == "Disarmed" and self.armed_drone_signal:
        self.state = "init"
        self.publish_task("init")
    
    elif self.state == "init":
        self.state = "takeoff"
        self.publish_task("takeoff")
    
    elif self.state == "takeoff":
        # Aquí podrías esperar un mensaje de que el dron ha despegado
        self.state = "aruco_nav"
        self.publish_task("aruco_navigation")
    
    elif self.state == "aruco_nav":
        # Llamar a la lógica para navegar hacia el ArUco
        self.state = "line_follow"
        self.publish_task("line_follow")
    
    elif self.state == "line_follow":
        # Llamar a la lógica para seguir la línea
        self.state = "final_task"
        self.publish_task("final_task")
    
    elif self.state == "final_task":
        # Realizar la tarea final (ej. aterrizaje o acción final)
        self.state = "mission_complete"
        self.publish_task("mission_complete")