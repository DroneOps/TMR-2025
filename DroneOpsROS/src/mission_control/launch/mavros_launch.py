from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mavros',
            executable='mavros_node',
            output='screen',
            parameters=[  # Asegúrate de que este bloque sea el adecuado
                '/opt/ros/humble/share/mavros/launch/apm_config.yaml',  # Carga parámetros YAML
                {
                    'fcu_url': 'udp://127.0.0.1:14550@',
                    'gcs_url': 'udp://@127.0.0.1:14555',
                    'target_system_id': 1,
                    'target_component_id': 1,
                    'fcu_protocol': 'v2.0'
                }
            ],
            arguments=['--ros-args', '--log-level', 'info']
        )
    ])

