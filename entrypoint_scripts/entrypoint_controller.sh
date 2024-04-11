#!/bin/bash

# Source the ROS2 installation
source /opt/ros/humble/setup.bash

# Source the ROS2 colcon workspace
source /colcon_ws/install/setup.bash



# Run additional commands

#ros2 run my_controller trial_controller_opti &
#ros2 run my_controller evaluation_node_odom
#ros2 run my_controller simplenode
#ros2 run my_controller trial_controller_backup_original
ros2 run my_controller trial_controller_diff
