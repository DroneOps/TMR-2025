from setuptools import find_packages, setup

package_name = 'my_aruco_detector'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='manuel',
    maintainer_email='manuel@todo.todo',
    description='A ROS 2 package for ArUco marker detection',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'aruco_detector = my_aruco_detector.aruco_detector:main'
        ],
    },
)

