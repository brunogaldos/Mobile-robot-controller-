# Mobile Robot Navigation with Optitrack System

## Overview

This project is part of a Master's thesis conducted at the WZL department in the Robotic Systems Engineering program at RWTH Aachen University. The aim is to develop a controller for mobile robot navigation.

## System Requirements

- ROS Version: Humble
- Gazebo Version: 11.11.0

## Project Structure

The project comprises two main packages:

1. **Simulation Package "my_bot":**
   - This package serves as the core application, running simulations in Gazebo.
   - It simulates the mobile robot in an empty world environment with a predefined setup.

2. **Controller Package "my_controller":**
   - This package includes the `trial_controller.py` node responsible for publishing topics to the mobile robot and controlling its movements.

## Setup Instructions

1. **Clone Repositories:**
   - Create a workspace and inside it, create a `src` directory.
   - Clone each package into the `src` directory.

2. **Build and Source:**
   - Build the packages inside the workspace.
   - Source the workspace.

3. **Launch Simulation Package kairos:**
   - A) For differential robot:
   - Execute the following command:
     ```sh
     ros2 launch my_bot launch_sim.launch.py
     ```

     ```

   - Gazebo will launch, displaying the mobile robot in the world environment. 

4. **Run Controller Node from the second package my_controller:**
   - Execute the following command:
     ```sh
     ros2 run my_controller trial_controller
     ```
   - The terminal will prompt you to enter the start pose, desired goal pose, and velocity. Enter each value in float format and press enter after each.

## Simulation Execution

- Upon launching the simulation package, Gazebo will display the mobile robot in the world environment. The robot is already subscribed to the topic messages.

- Running the controller node allows the user to input the start pose, desired goal pose, and velocity. Follow the prompts in the terminal, entering float values for each parameter and pressing enter.



<video src="Screencast%20from%2022-01-24%2017-56-16-2.mp4" controls title="Title"></video>




![Screencast_from_22-01-24_17_56_16](/uploads/f67ef8e1b626b40f1099246a9fd1c1c0/Screencast_from_22-01-24_17_56_16.webm)

## Further steps and development



- Use the controller with optitrack instead of given poses, currently the controller has been tested in the real robot KairosAB
</br></br>

---


