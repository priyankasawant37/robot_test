from toy_robot.config import *

def place_cmd_excecuted(method):
    """Decorator to check if place cmd is excecuted"""
    def wrapper(self):
        if self.x == None or self.y  == None or self.face == None:
            return
        method(self)

    return wrapper

def get_rotate_face(current_face, rotation_direction):
    """Gives the new direction the robot faces on rotating 90 degrees to the rotation_direction"""
    rotate_to_face = None
    direction_face_mapping = {
    'NORTH': {
        'LEFT': 'WEST',
        'RIGHT': 'EAST'
        },
    'EAST': {
        'LEFT': 'NORTH',
        'RIGHT': 'SOUTH'
        },
    'SOUTH': {
        'LEFT': 'EAST',
        'RIGHT': 'WEST'
        },

    'WEST': {
        'LEFT': 'SOUTH',
        'RIGHT': 'NORTH'
        }
    }
    rotate_to_face = direction_face_mapping[current_face][rotation_direction]
    return rotate_to_face


class Robot(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.face = None

    def __str__(self):
        return "{},{},{}".format(self.x, self.y, self.face)



    def place(self, coordinates, face):
        """Put the toy robot on the table in position X,Y and facing NORTH, SOUTH, EAST or WEST."""
        x, y = coordinates
        try:
            if x>=grid_min and  x<grid_max:
                self.x = x
            else:
                raise InvalidPosition
            if  y>=grid_min  and  y<grid_max:
                self.y = y
            else:
                raise InvalidPosition
            if face in possible_directions:
                self.face = face
            else:
                raise InvalidPosition
        except InvalidPosition:
            pass

    @place_cmd_excecuted
    def report(self):
        """Print the current position of the robot"""
        print(self)


    @place_cmd_excecuted
    def move(self):
        """Move the toy robot one unit forward in the direction it is currently facing."""
        try:
            if self.face == 'NORTH' and self.y<grid_max:
                self.y += 1
            elif self.face == 'EAST' and self.x<grid_max:
                self.x += 1
            elif self.face == 'SOUTH' and self.y>grid_min:
                self.y -= 1
            elif self.face == 'WEST' and self.x>grid_min:
                self.x -= 1
            else:
                raise InvalidPosition

        except InvalidPosition:
            pass


    @place_cmd_excecuted
    def left(self):
        """Rotate the robot 90 degrees to the left direction without changing the position."""
        rotate_to_face = get_rotate_face(self.face, 'LEFT')
        if rotate_to_face:
            self.face = rotate_to_face
        else:
            raise InvalidPosition


    @place_cmd_excecuted
    def right(self):
        """Rotate the robot 90 degrees to the right direction without changing the position"""
        rotate_to_face = get_rotate_face(self.face,'RIGHT')
        if rotate_to_face:
            self.face = rotate_to_face
        else:
            raise InvalidPosition



class InvalidPosition(Exception):
    """Raised when a position is given does not fit the table grid size"""
    pass

if __name__ == "__main__":

    r = Robot()
    r.place( (1,3), 'NORTH')
    r.move()
    r.report()
    r.left()
    r.report()
    r.move()
    r.report()
    r.left()
    r.report()
