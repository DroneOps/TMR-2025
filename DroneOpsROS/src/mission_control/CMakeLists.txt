cmake_minimum_required(VERSION 3.8)
project(mission_control)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rclpy REQUIRED)

# Generate services
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/Altitud.srv"
)

# Install Python package directory
install(DIRECTORY mission_control/
  DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch)

# Install executables with renamed targets
install(PROGRAMS
  mission_control/takeoff.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME takeoff
)

install(PROGRAMS
  mission_control/arm_drone.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME arm_drone
)

install(PROGRAMS
  mission_control/mission_manager.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME mission_manager
)

ament_package()