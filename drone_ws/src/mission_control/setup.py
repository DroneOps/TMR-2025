from setuptools import find_packages, setup

package_name = 'mission_control'

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
    maintainer_email='a01645677@tec.mx',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'arm_drone = mission_control.arm_drone:main',
        	'mission_manager = mission_control.mission_manager:main',
        ],
    },
)
