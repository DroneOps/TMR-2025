from setuptools import setup
import os
from glob import glob

package_name = 'mission_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include launch files
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py') + glob('launch/*.py')),
        # Include config files
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml') + glob('config/*.yml')),
        # CORRECTED: Service files (assuming srv/ is at package root)
        (os.path.join('share', package_name, 'srv'), glob('srv/*.srv')),  # ← Fix here
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'arm_drone = mission_control.arm_drone:main',
            'mission_manager = mission_control.mission_manager:main',
            'takeoff = mission_control.takeoff:main',
        ],
    },
)