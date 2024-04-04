import os
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
import logging
def generate_launch_description():
    try:
        return LaunchDescription([


            DeclareLaunchArgument(
                'x', default_value='1.0', description='X coordinate of the goal pose'
            ),
            DeclareLaunchArgument(
                'y', default_value='1.0', description='Y coordinate of the goal pose'
            ),
            DeclareLaunchArgument(
                'theta', default_value='0.0', description='Theta of the goal pose'
            ),
            DeclareLaunchArgument(
                'velocity', default_value='1.0', description='velocity of the goal pose'
            ),



            Node(
                package='my_controller',
                executable='trial_controller',
                parameters=[
                    {'x': LaunchConfiguration('x')},
                    {'y': LaunchConfiguration('y')},
                    {'theta': LaunchConfiguration('theta')},
                    {'velocity': LaunchConfiguration('velocity')}
                    # other parameters here
                ]
            )

        ])
    except Exception as e: 
        logging.error("An error ocurred:"+str(e))
        raise


