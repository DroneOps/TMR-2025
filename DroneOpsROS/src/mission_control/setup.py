from setuptools import setup
import os
from setuptools import setup
import os
from glob import glob

package_name = 'mission_control'

# Crear directorios necesarios si no existen
os.makedirs('resource', exist_ok=True)
os.makedirs('launch', exist_ok=True)

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
   data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Incluir todos los archivos de lanzamiento
        (os.path.join('share', package_name, 'launch'), 
         glob('launch/*.launch.py') + glob('launch/*.py')),
        # Incluir archivos de configuración si los tienes
        (os.path.join('share', package_name, 'config'), 
         glob('config/*.yaml') + glob('config/*.yml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='root',
    maintainer_email='root@todo.todo',
    description='High Level Decisions Package for drone',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'arm_drone = mission_control.arm_drone:main',
            'mission_manager = mission_control.mission_manager:main',
        ],
    },
)
