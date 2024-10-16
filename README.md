# Indoor Simulation

## Author & Notes
Jeongbin Son  
Course: CS 460  
Project Part 1: Indoor Environment

## Description

This package is for running an indoor simulation environment that models after the floor of Rodgers Library at the University of ALabama. This package launches webots in the user's host computer.


## Commands to run this package

1) source /opt/ros/humble/setup.bash

2) [within host laptop and not in ubuntu]:
export WEBOTS_HOME=/Applications/Webots.app
python3 local_simulation_server.py

3) cd ~/ros2_ws
4) colcon build
5) source install/setup.bash
6) ros2 launch indoor_simulation indoor_launch.py
