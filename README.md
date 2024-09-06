# Mobile Robot Navigation with motion tracking System

## Overview

This project is part of a Master's thesis conducted at the WZL department in the Robotic Systems Engineering program at RWTH Aachen University. The aim is to develop a controller for mobile robot navigation using motion capture system. The following symulation is part of the pilot testing with controller capable of obstacle avoidace for mobile robot navigation.

## System Requirements

- ROS2 Version: Humble
- Gazebo Version: 11.11.0

## Project Structure

The project comprises two main packages:

1. **Simulation Package "my_bot":**
   - This package serves as the core application, running simulations in Gazebo.
   - It simulates the mobile robot in an empty world environment with a predefined setup.

2. **Controller Package "my_controller":**
   - This package includes the `trial_controller_diff.py` node responsible for publishing topics to the mobile robot and controlling its movements.

## Setup Instructions

1. **Clone Repositories:**

   - Clone the repository into your directory.

3. **Build and Launch:*
   - Build the docker image
   - Launch the simulation along with the controller for that inside the directory execute:
     ```sh
     cd docker_run
     ``` 

     ```sh
     ./run_mocap.driver.sh
     ```
4. **Launch Simulation Package kairos locally:**
   - We can also run the nodes and the launch file locally, by runnning the container and then executing the following:
   - A) For differential robot:
   - Execute the following command:
     ```sh
     ros2 launch my_bot launch_sim.launch.py
     ```


   - Gazebo will launch, displaying the mobile robot in the world environment. 

6. **Run Controller Node from the second package my_controller:**
   - Execute the following command:
     ```sh
     ros2 run my_controller trial_controller_diff
     ```
   - The terminal will prompt you to enter the start pose, desired goal pose, and velocity. Enter each value in float format and press enter after each.

## Simulation Execution

- Upon launching the simulation package, Gazebo will display the mobile robot in the world environment. The robot is already subscribed to the topic messages.

- Running the controller node allows the user to input the start pose, desired goal pose, and velocity. Follow the prompts in the terminal, entering float values for each parameter and pressing enter.



<video src="Screencast%20from%2022-01-24%2017-56-16-2.mp4" controls title="Title"></video>


[Screencast from 31-08-24 09_41_44.webm](https://github.com/user-attachments/assets/35361dce-7986-44d0-8b3d-a966d67b6107)





