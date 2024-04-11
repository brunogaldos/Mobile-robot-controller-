#!/bin/bash

# Source the ROS2 installation
source /opt/ros/humble/setup.bash

# Source the ROS2 colcon workspace
source /colcon_ws/install/setup.bash



# Run additional commands

ros2 launch my_bot launch_sim.launch.py &
ros2 run my_controller trial_controller_diff
