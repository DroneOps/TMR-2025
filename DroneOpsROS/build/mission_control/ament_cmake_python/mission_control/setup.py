from setuptools import find_packages
from setuptools import setup

setup(
    name='mission_control',
    version='0.0.0',
    packages=find_packages(
        include=('mission_control', 'mission_control.*')),
)
