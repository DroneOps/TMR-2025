
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from mavros_msgs.msg import State
from std_msgs.msg import Float64
from rclpy.qos import QoSProfile
from rclpy.qos import QoSDurabilityPolicy, QoSReliabilityPolicy
from rclpy.qos import QoSHistoryPolicy



class Takeoff():
    def __init__(self):
         super().__init__('takeoff') 
         self.target_altitude = 1.0  # Altura objetivo de despegue
         self.throttle = 0.0  # Inicializamos el throttle en 0
         

         self.increase_throttle_until_altitude() 
        


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