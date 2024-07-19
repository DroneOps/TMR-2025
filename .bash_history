sudo
sudo install google
sudo apt google-chrome
sudo apt upgrade
sudo apt update
sudo apt upgrade
wget
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt install git
git clone https://github.com/ArduPilot/ardupilot.git
cd ardupilot
Tools/environment_install/install-prereqs-ubuntu.sh -y
. ~/.profile
git checkout Copter-4.0.4
git submodule update --init --recursive
git checkout Copter-4.0.4
git submodule update --init --recursive
ping github.com
git submodule update --init --recursive
cd /home/manuel/ardupilot/modules
git clone https://github.com/ArduPilot/libcanard.git
git clone https://github.com/ArduPilot/uavcan.git
cd /home/manuel/ardupilot
git submodule update --init --recursive
cd ~/ardupilot/ArduCopter
sim_vehicle.py -w
clear
cd ..
sudo sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
wget http://packages.osrfoundation.org/gazebo.key -O - | sudo apt-key add -
sudo apt upgrade
sudo apt-get install gazebo11 libgazebo11-dev
clear
gazebo
clear
git clone https://github.com/khancyr/ardupilot_gazebo.git
cd ardupilot_gazebo
mkdir build
cd build
cmake ..
make -j4
sudo make install
echo 'export GAZEBO_MODEL_PATH=~/ardupilot_gazebo/models' >> ~/.bashrc
. ~/.bashrc
gazebo --verbose ~/ardupilot_gazebo/worlds/iris_arducopter_runway.world
clear
cd ../../..
cd ..
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/
ros-latest.list'
clear
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/
ros-latest.list'
ros-latest.list'

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/
sudo apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
sudo apt update
sudo apt install ros-noetic-desktop-full
sudo apt install ros-noetic-PACKAGE
sudo apt install ros-noetic-slam-gmapping
source /opt/ros/noetic/setup.bash
sudo apt-get update
sudo apt-get install git
sudo apt-get install gitk git-gui
roslaunch iq_sim myLaunch.launch
sudo usermod -a -G dialout $USER
sudo apt-get remove modemmanager
wget https://s3-us-west-2.amazonaws.com/qgroundcontrol/latest/QGroundControl.AppImage
chmod +x ./QGroundControl.AppImage 
./QGroundControl.AppImage 
source .bashrc
cd ardupilot
. ~/.profile
git checkout Copter-4.0.4
git submodule update --init --recursive
cd ~/ardupilot/ArduCopter/ && sim_vehicle.py -v ArduCopter -f gazebo-iris --console
roslaunch iq_sim runway.launch
cd ~/ardupilot/ArduCopter/ && sim_vehicle.py -v ArduCopter -f gazebo-iris --console
sim_vehicle.py 
source /opt/ros/noetic/setup.bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
clear
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
sudo apt install python3-rosdep
sudo rosdep init
rosdep update
clear
sudo apt-get install python3-wstool python3-rosinstall-generator python3-catkin-lint python3-pip python3-catkin-tools
pip3 install osrf-pycommon
clear
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws
catkin init
wstool init ~/catkin_ws/src
rosinstall_generator --upstream mavros | tee /tmp/mavros.rosinstall
rosinstall_generator mavlink | tee -a /tmp/mavros.rosinstall
wstool merge -t src /tmp/mavros.rosinstall
wstool update -t src
rosdep install --from-paths src --ignore-src --rosdistro `echo $ROS_DISTRO` -y
catkin build
echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc
sudo ~/catkin_ws/src/mavros/mavros/scripts/install_geographiclib_datasets.sh
cd ~/catkin_ws/src
git clone https://github.com/Intelligent-Quads/iq_sim.git
echo "GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:$HOME/catkin_ws/src/iq_sim/models" >> ~/.bashrc
catkin build
source ~/.bashrc
clear
roslaunch iq_sim runway.launch
clear
cd ../..
cd ..
cd ~/ardupilot/ArduCopter/ && sim_vehicle.py -v ArduCopter -f gazebo-iris --console
roslaunch iq_sim runway.launch
clear
cd ~/ardupilot/ArduCopter/ && sim vehicle.py -v ArduCopter -f gazebo-iris --console
clear
cd ~/ardupilot/ArduCopter/ && si_m vehicle.py -v ArduCopter -f gazebo-iris --console
cd ~/ardupilot/ArduCopter/ && sim_vehicle.py -v ArduCopter -f gazebo-iris --console
clear
cd ~/ardupilot/ArduCopter/ && sim_vehicle.py -v ArduCopter -f gazebo-iris --console
source .bashrc
cd ~/ardupilot/ArduCopter/ && sim_vehicle.py -v ArduCopter -f gazebo-iris --console
cd ~/ardupilot/ArduCopter/ 
ls
clear
cd ../..
cd ..
