#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CameraNode(Node):
    def __init__(self):
        super().__init__('camera_node')
        
        # Publicador de imágenes en el tópico "/image_raw"
        self.publisher = self.create_publisher(Image, 'camera/image', 10)
        
        # Inicializar OpenCV y el puente CvBridge
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture(0)  # Capturar desde la cámara de la laptop
        
        # Verificar que la cámara se abrió correctamente
        if not self.cap.isOpened():
            self.get_logger().error("No se pudo abrir la cámara")
            return
        
        # Publicar imágenes cada 0.1 segundos (10 FPS)
        self.timer = self.create_timer(0.1, self.publish_frame)
        
    def publish_frame(self):
        ret, frame = self.cap.read()
        if ret:
            # Convertir imagen OpenCV a mensaje ROS
            img_msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher.publish(img_msg)
            self.get_logger().info("Imagen publicada")
            
            # Mostrar la imagen en una ventana de OpenCV
            cv2.imshow("Camera Feed", frame)
            cv2.waitKey(1)  # Esto asegura que OpenCV se actualice correctamente
        else:
            self.get_logger().error("Error al capturar imagen")
    
    def destroy_node(self):
        self.cap.release()
        cv2.destroyAllWindows()  # Cerrar la ventana de OpenCV al destruir el nodo
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = CameraNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
