#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImageViewer(Node):
    def __init__(self):
        super().__init__('image_viewer')
        self.bridge = CvBridge()
        # Subscriber to raw camera images
        self.subscription = self.create_subscription(
            Image,
            '/camera/image',
            self.listener_callback,
            10)
        # Publisher for processed images
        self.publisher = self.create_publisher(Image, '/camera/corrected_image', 10)
        self.subscription  # Avoid unused variable warning

    def listener_callback(self, msg):
        try:
            # Convert ROS Image to OpenCV image (RGB)
            cv_image = self.bridge.imgmsg_to_cv2(msg, 'rgb8')
            # Convert RGB to BGR (OpenCV format)
            cv_image = cv2.cvtColor(cv_image, cv2.COLOR_RGB2BGR)

            # Get image dimensions and center
            height, width = cv_image.shape[:2]
            center = (width // 2, height // 2)

            # Set rotation angle (adjust as needed)
            rotation_angle = 265.0

            # Create the rotation matrix
            rotation_matrix = cv2.getRotationMatrix2D(center, rotation_angle, 1.0)

            # Compute new image dimensions to prevent cropping
            cos = abs(rotation_matrix[0, 0])
            sin = abs(rotation_matrix[0, 1])
            new_width = int((height * sin) + (width * cos))
            new_height = int((height * cos) + (width * sin))

            # Adjust the rotation matrix for translation
            rotation_matrix[0, 2] += (new_width / 2) - center[0]
            rotation_matrix[1, 2] += (new_height / 2) - center[1]

            # Rotate the image
            rotated_image = cv2.warpAffine(cv_image, rotation_matrix, (new_width, new_height))

            # Display the processed image
            cv2.imshow("Corrected Camera View", rotated_image)
            cv2.waitKey(1)

            # Convert back to ROS Image message and publish
            corrected_msg = self.bridge.cv2_to_imgmsg(rotated_image, encoding="bgr8")
            self.publisher.publish(corrected_msg)

        except Exception as e:
            self.get_logger().error(f'Error processing image: {e}')

def main(args=None):
    rclpy.init(args=args)
    image_viewer = ImageViewer()
    rclpy.spin(image_viewer)
    image_viewer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

