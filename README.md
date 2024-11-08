# Indoor Simulation

## Author & Notes
Jeongbin Son  
Course: CS 460  
Project Part 2: Outdoor Environment

## Description

This package is for running an outdoor simulation environment that models after a 0.5 square mile radius of the city of Tuscaloosa in Alabama. This package launches webots in the user's host computer.


## Commands to run this package

Within your host laptop:
1) export WEBOTS_HOME=/Applications/Webots.app
2) python3 local_simulation_server.py


Within your ubuntu vm:
3) cd ~/ros2_ws
4) colcon build
5) source install/setup.bash
6) ros2 launch outdoor_simulation outdoor_launch.py


## Updating Parameters in the World File

Users can also modify various parameters in the `cs460pp2.wbt` file.


### Modifying Ceiling Traffic Light Parameters

If you wanted to adjust the traffic lights and how to change the starting color or the duration of the lights, you can modify the code with a text editor.

TrafficLightBigPole {
  translation -360.297 572.725 0
  rotation 0 0 1 -2.7489003061004254
  name "traffic light big pole test"
  slot2 [
    GenericTrafficLight {
      translation 0 2.49 0.250007
      rotation 1 0 0 1.5708
      state "red"
    }
  ]
  slot3 [
    GenericTrafficLight {
      translation 0 2.58 0.210009
      rotation 1 0 0 1.5708
      name "generic traffic light(1)"
      state "red"
    }
  ]
}

- **`startGreen`**: You can modify this parameter to be True or False. Setting this to false would make this traffic light start on Red.

- **`greenTime`**: You can modify this parameter and raise or decrease the integer value. A higher integer would give the trafflic light a longer time to show Green before it turns Red.

- **`redTime`**: You can modify this parameter and raise or decrease the integer value. A higher integer would give the trafflic light a longer time to show Red before it turns Green.

- **`state`**: You can modify this parameter and designate a value of 'red' or 'green'. Setting this parameter to 'red' would let this traffic light start on the color red.



### Modifying Ceiling Street Light Parameters

If you wanted to adjust the street lights and how to change the intensity, beamWidth, etc, it is easy to do so in a text editor.

- **`beamWidth`**: You can modify this parameter to be an integer value. Setting this to a higher value would allow the beam to be wider.

- **`intensity`**: You can modify this parameter and raise or decrease the integer value. A higher integer would give the street light a brighter point of light.