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



## Updating Parameters in the World File

Users can also modify various parameters in the `rodgers.wbt` file.


### Modifying Ceiling Light Parameters

If you wanted to adjust `CeilingLight` and how bright the lights were implemented, you can modify the following parameter:

CeilingLight {
  translation -4.6441 -2.2406 4.18   
  name "ceiling light 1"             
  pointLightIntensity 12              # Adjusts the light intensity (default: 12)
}

- **`pointLightIntensity`**: You can increase/decreaes this value to change how "bright" the different sources of light on screen is.

### Modifying Door Properties

You can calso modify whether a door can be opened or not by modifying the following:


Door {
  openable true  # Set to true to allow opening, false to make it non-openable
}
