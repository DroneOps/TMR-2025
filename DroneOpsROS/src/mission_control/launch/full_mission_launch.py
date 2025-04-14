from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mission_control',
            executable='arm_drone',
            name='arm_drone_node',
            output='screen'
        ),
        Node(
            package='mission_control',
            executable='takeoff',
            name='takeoff_node',
            output='screen'
        ),
        Node(
            package='mission_control',
            executable='mission_manager',
            name='mission_manager_node',
            output='screen'
        )
    ])

