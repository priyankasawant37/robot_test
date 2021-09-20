from toy_robot.config import *

class CommandParser(object):

    def __init__(self, line):
        cmd, coordinates, direction = self.get_cmd_args(line)
        self.cmd = cmd
        self.coordinates = coordinates
        self.direction = direction


    def __str__(self):
        return "Action: {}\nCoordinates: {}\nDirection: {}\n".format(self.cmd, self.coordinates, self.direction)


    def get_cmd_args(self, line=None):
        cmd = ''
        args = []
        coordinates = (None, None)
        direction = None

        if line:

            cmd_list = line.strip().split()

            if not len(cmd_list):
                raise InputError
            cmd = self._is_valid_action(cmd_list[0].strip())
            if cmd == 'PLACE':
                if len(cmd_list) < 2:
                    raise InputError
                args = cmd_list[1].split(',')

                int_args = self._is_valid_place_args(args)

                coordinates = int_args
                direction = self._is_valid_direction(args[2].strip())


            else:
                coordinates = (None, None)
                direction = None

        return cmd, coordinates, direction

    def _is_valid_action(self, cmd):
        if cmd not in allowed_actions:
            raise InputError
        return cmd

    def _is_valid_direction(self, direction):
        if direction not in possible_directions:
            raise InputError
        return direction

    def _is_valid_place_args(self, args):

        if len(args) != 3:
            raise InputError

        if not args[0].isdigit()  or not args[1].isdigit():
            raise InputError
        else:
            x = int(args[0])
            y = int(args[1])

        return (x,y)






class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input."""
    pass


if __name__ == "__main__":
    c =CommandParser('PLACE 0,0,NORTH')
    print(c)
    c = CommandParser('MOVE')
    print(c)
    c = CommandParser('REPORT')
    print(c)
    c = CommandParser('REPORT 3,4,NORTH')

    print(c)
    # print(c.parse('PLACE 0,0,eNORTH'))
    # print(c.parse('MOVE'))
