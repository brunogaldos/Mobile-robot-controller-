import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    # Include the robot_state_publisher launch file, provided by our own package. Force sim time to be enabled
    # !!! MAKE SURE YOU SET THE PACKAGE NAME CORRECTLY !!!
    package_name = 'my_controller'  # <--- CHANGE ME
    
    # Run the spawner node from the gazebo_ros package. The entity name doesn't really matter if you only have a single robot.
    evaluation_slam = Node(
        package=package_name,
        executable='evaluation_node_slam',
        output='screen'
    )
    
    evaluation_odom = Node(
        package=package_name,
        executable='evaluation_node_odom',
        output='screen'
    )
    """
    trial_controller_1 = Node(
        package=package_name,
        executable='trial_controller',
        name='trial_controller_1',  # Fixed the name
        parameters=[
            
            {'goal_pose': {'x': -2.0, 'y': -1.5, 'theta': 0.0}}],
        output='screen'
    )
    
    trial_controller_2 = Node(
        package=package_name,
        executable='trial_controller',
        name='trial_controller_2',  # Fixed the name
        parameters=[{'goal_pose': {'x': 2.5, 'y': -2.0, 'theta': 0.0}}],
        output='screen'
    )
    
    
    trial_controller_3 = Node(
        package=package_name,
        executable='trial_controller',
        name='trial_controller_3',  # Fixed the name
        
        #parameters=[{'goal_pose': {'x': 2.0, 'y': 3.0, 'theta': 0.0}}],
        output='screen'
    )
     """
    # Code for delaying a node (I haven't tested how effective it is)
    # First add the below lines to imports
    # from launch.actions import RegisterEventHandler
    # from launch.event_handlers import OnProcessExit
    #
    # Then add the following below the current diff_drive_spawner
    # delayed_diff_drive_spawner = RegisterEventHandler(
    #     event_handler=OnProcessExit(
    #         target_action=spawn_entity,
    #         on_exit=[diff_drive_spawner],
    #     )
    # )
    #
    # Replace the diff_drive_spawner in the final return with delayed_diff_drive_spawner

    # Launch them all!
    return LaunchDescription([

       
        evaluation_odom,
        evaluation_slam
    ])
