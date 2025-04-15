from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Node from the mission_control package (arm_drone node)
        Node(
            package='mission_control',
            executable='arm_drone',
            name='arm_drone_node',
            output='screen'
        ),
       
        # Node from the control_system package (e.g., a lateral controller)
        Node(
            package='control_system',
            executable='control_aruco',
            name='control_aruco_node',
            output='screen'
        ),
        
        Node(
            package='control_system',
            executable='control_takeoff',
            name='control_takeoff_node',
            output='screen'
        ),
        # Node from the vision_system package
        Node(
            package='vision_system',
            executable='aruco_detector',
            name='camera_aruco',
            output='screen'
        )
    ])

