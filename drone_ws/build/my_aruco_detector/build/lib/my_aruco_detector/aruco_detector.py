#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import Int32MultiArray
from cv_bridge import CvBridge
import numpy as np
import cv2
import math

# Define target markers with their sizes in cm
target_markers = {
    100: 15,    # ID 100 with 15cm size
    105: 15     # ID 105 with 15cm size
}

# Rotation matrix utilities
def isRotationMatrix(R):
    Rt = np.transpose(R)
    shouldBeIdentity = np.dot(Rt, R)
    I = np.identity(3, dtype=R.dtype)
    n = np.linalg.norm(I - shouldBeIdentity)
    return n < 1e-6

def rotationMatrixToEulerAngles(R):
    assert(isRotationMatrix(R))
    sy = math.sqrt(R[0, 0] * R[0, 0] + R[1, 0] * R[1, 0])
    singular = sy < 1e-6
    if not singular:
        x = math.atan2(R[2, 1], R[2, 2])
        y = math.atan2(-R[2, 0], sy)
        z = math.atan2(R[1, 0], R[0, 0])
    else:
        x = math.atan2(-R[1, 2], R[1, 1])
        y = math.atan2(-R[2, 0], sy)
        z = 0
    return np.array([x, y, z])

class ArucoDetectorNode(Node):
    def __init__(self):
        super().__init__('aruco_detector')
        self.bridge = CvBridge()

        # Subscribe to a camera image topic (update topic if needed)
        self.subscription = self.create_subscription(
            Image,
            '/camera/image',
            self.image_callback,
            10)
        self.subscription  # Prevent unused variable warning

        # Publisher for marker information using Int32MultiArray
        self.marker_info_publisher = self.create_publisher(Int32MultiArray, '/marker_info', 10)

        # Camera parameters (default values)
        self.camera_width = 1280
        self.camera_height = 720
        focal_length = self.camera_width
        self.camera_matrix = np.array([
            [focal_length, 0, self.camera_width / 2],
            [0, focal_length, self.camera_height / 2],
            [0, 0, 1]
        ], dtype=np.float32)
        self.camera_distortion = np.zeros((1, 5), dtype=np.float32)

        # Try to load calibration files if available
        try:
            calib_path = ""  # Set to your calibration file directory
            self.camera_matrix = np.loadtxt(calib_path + 'cameraMatrix_webcam.txt', delimiter=',')
            self.camera_distortion = np.loadtxt(calib_path + 'cameraDistortion_webcam.txt', delimiter=',')
            self.get_logger().info("Camera calibration loaded successfully")
        except Exception as e:
            self.get_logger().warn("Using default camera calibration: " + str(e))

        # 180° rotation matrix around the x-axis
        self.R_flip = np.array([[1,  0,  0],
                                [0, -1,  0],
                                [0,  0, -1]], dtype=np.float32)

        # Define the ArUco dictionary and detector (using the modern API)
        self.aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_5X5_250)
        self.aruco_params = cv2.aruco.DetectorParameters()
        self.detector = cv2.aruco.ArucoDetector(self.aruco_dict, self.aruco_params)

        self.font = cv2.FONT_HERSHEY_PLAIN

    def image_callback(self, msg):
        try:
            # Convert ROS Image to OpenCV image (BGR format)
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Detect ArUco markers
            corners, ids, rejected = self.detector.detectMarkers(gray)

            # Prepare an array to publish marker info.
            # Each marker provides: [marker_id, x, y, yaw]
            marker_data = []

            if ids is not None and len(ids) > 0:
                # Process each detected marker
                for i, marker_id in enumerate(ids.flatten()):
                    if marker_id in target_markers:
                        marker_size = target_markers[marker_id]
                        # Estimate pose for this marker
                        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(
                            [corners[i]], marker_size, self.camera_matrix, self.camera_distortion)
                        rvec, tvec = rvecs[0], tvecs[0]

                        # Calculate rotation matrix and Euler angles for marker attitude
                        R_ct = np.matrix(cv2.Rodrigues(rvec)[0])
                        R_tc = R_ct.T
                        # Correct orientation using R_flip and extract Euler angles
                        euler_angles = rotationMatrixToEulerAngles(self.R_flip @ R_tc)
                        # Extract yaw (rotation about the z-axis) and convert to degrees
                        yaw_marker = math.degrees(euler_angles[2])

                        # Get x and y positions from the translation vector
                        x_marker = tvec[0][0]
                        y_marker = tvec[0][1]

                        # Append marker data (converted to int)
                        marker_data.extend([
                            int(marker_id),
                            int(x_marker),
                            int(y_marker),
                            int(yaw_marker)
                        ])

            # Publish the marker information if any marker was detected
            if marker_data:
                msg_to_publish = Int32MultiArray()
                msg_to_publish.data = marker_data
                self.marker_info_publisher.publish(msg_to_publish)
                self.get_logger().info("Published marker info: " + str(marker_data))

            # Optionally, if you don't want to display the processed image, comment out the next two lines:
            # cv2.imshow("Aruco Detection", frame)
            # cv2.waitKey(1)

        except Exception as e:
            self.get_logger().error("Error in image callback: " + str(e))

def main(args=None):
    rclpy.init(args=args)
    node = ArucoDetectorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

