from setuptools import find_packages
from setuptools import setup

setup(
    name='control_system',
    version='0.0.0',
    packages=find_packages(
        include=('control_system', 'control_system.*')),
)
