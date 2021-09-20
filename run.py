import sys
from toy_robot.command_parser import CommandParser, InputError
from toy_robot.robot import Robot, InvalidPosition

def main():
    robot = Robot()

    for line in sys.stdin:
        try:
            parse_cmd = CommandParser(line)
            if parse_cmd.cmd == 'PLACE':
                robot.place(parse_cmd.coordinates,  parse_cmd.direction)
            else:
                getattr(robot, parse_cmd.cmd.lower())()
        except InputError:
            pass
            

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:

      print('\nGood Bye World!')
