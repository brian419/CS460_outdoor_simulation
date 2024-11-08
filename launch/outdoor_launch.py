#!/usr/bin/env python

import os
from launch import LaunchDescription
from webots_ros2_driver.webots_launcher import WebotsLauncher
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_dir = get_package_share_directory('outdoor_simulation')  
    world_file = os.path.join(package_dir, 'worlds', 'cs460pp2.wbt')  

    webots = WebotsLauncher(
        world=world_file,
        ros2_supervisor=True
    )

    return LaunchDescription([
        webots
    ])
