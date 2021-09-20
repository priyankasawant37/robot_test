# Toy Robot Code Challenge

## Problem Statement

The application is a simulation of a toy robot moving on a square table top, of dimensions 5 units x 5 units. There are no
other obstructions on the table surface. The robot is free to roam around the surface of the table, but must be prevented
from falling to destruction. Any movement that would result in the robot falling from the table must be prevented,
however further valid movement commands must still be allowed.

## Folder Structure

    ├── README.md
    ├── requirements.text  
    ├── run.py #takes input from stdin
    ├── testing  
    │   ├── __init__.py
    │   ├── test_cmds.py #tests for command validations
    │   └── test_robot.py #tests for robot.py 
    ├── toy_robot
    │   ├── command_parser.py #reads and processes commands
    │   ├── config.py #config varaibles
    │   ├── __init__.py
    │   └── robot.py #main Robot class
    └── venv

## Constraints

The toy robot must not fall off the table during movement. This also includes the initial placement of the toy robot. Any
move that would cause the robot to fall must be ignored.

## Commands

- PLACE :  It will put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST.

- MOVE : It will move the toy robot one unit forward in the direction it is currently facing.

- LEFT : It will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

- RIGHT : It will rotate the robot 90 degrees in the specified direction without changing the position of the robot.

- REPORT : It will announce the X,Y and F of the robot


- Application can read in commands of the following form:

      PLACE X,Y,F
      MOVE
      LEFT
      RIGHT
      REPORT



## Usage


To setup your virtual environment:

    virtualenv venv

To activate your virtual environment:

    source venv/bin/activate

To install requirements:

    pip3 install -r requirements.text

To run tests:

    pytest -v testing

To provide input from stdin:

    python3 run.py

    PLACE 0,0,NORTH
    MOVE
    REPORT
    
    Output: 0,1,NORTH
