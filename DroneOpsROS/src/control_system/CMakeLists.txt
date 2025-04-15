cmake_minimum_required(VERSION 3.8)
project(control_system)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rclpy REQUIRED)

# Generate services
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/Altitud.srv"
)

# Install Python package directory
install(DIRECTORY control_system/
  DESTINATION lib/${PROJECT_NAME}
)

install(PROGRAMS
  control_system/control_aruco.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME control_aruco
)

install(PROGRAMS
  control_system/control_land.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME control_land
)

install(PROGRAMS
  control_system/control_takeoff.py
  DESTINATION lib/${PROJECT_NAME}
  RENAME control_takeoff
)


ament_package()
