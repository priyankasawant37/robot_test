#! ../env/bin/python
import pytest

@pytest.fixture
def robot():
    """Fixture giving instance of the Robot class"""
    from toy_robot.robot import Robot
    from toy_robot.command_parser import CommandParser
    return Robot()


@pytest.fixture
def command_parser():
    """Fixture giving instance of the Robot class"""
    from toy_robot.command_parser import CommandParser, InputError
    return CommandParser('')

class TestPlacement:

    def test_valid_place(self, robot, command_parser , capsys):
        #tests at random point on grid facing random direction
        command_parser.coordinates = (1,3)
        command_parser.direction = 'SOUTH'
        robot.place(command_parser.coordinates,  command_parser.direction)
        robot.report()

        out, err = capsys.readouterr()
        assert out == '1,3,SOUTH\n'

        #tests at random point on grid facing random direction
        command_parser.coordinates = (0,0)
        command_parser.direction = 'SOUTH'
        robot.place(command_parser.coordinates,  command_parser.direction)
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,SOUTH\n'


    def test_invalid_place(self, robot, command_parser , capsys):
        #set initial place 0,0, North
        command_parser.coordinates = (0,0)
        command_parser.direction = 'NORTH'
        robot.place(command_parser.coordinates,  command_parser.direction)
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,NORTH\n'

        #tets off the grid placement
        command_parser.coordinates = (10,10)
        robot.place(command_parser.coordinates, command_parser.direction)
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,NORTH\n'
        assert err == ''

        #tests edge case for grid_max
        command_parser.coordinates = (5,0)
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,NORTH\n'
        assert err == ''
        #tets wrong facing direction
        command_parser.direction = 'UP'
        robot.place(command_parser.coordinates, command_parser.direction)
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,NORTH\n'
        assert err == ''

        #tests negative position provided
        command_parser.coordinates = (-1,-1)
        command_parser.direction = 'NORTH'
        robot.place(command_parser.coordinates, command_parser.direction)
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,NORTH\n'
        assert err == ''



class TestMovement:
    def test_example_a(self, robot, command_parser , capsys):
        command_parser.coordinates = (0,0)
        command_parser.direction = 'NORTH'
        robot.place(command_parser.coordinates, command_parser.direction)
        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,1,NORTH\n'


    def test_example_b(self, robot, command_parser , capsys):
        command_parser.coordinates = (0,0)
        command_parser.direction = 'NORTH'
        robot.place(command_parser.coordinates, command_parser.direction)
        robot.left()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '0,0,WEST\n'


    def test_example_c(self, robot, command_parser , capsys):
        command_parser.coordinates = (1,2)
        command_parser.direction = 'EAST'
        robot.place(command_parser.coordinates, command_parser.direction)
        robot.move()
        robot.move()
        robot.left()
        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == '3,3,NORTH\n'

    def test_no_place_provided(self, robot, capsys):

        robot.report()
        out, err = capsys.readouterr()
        assert out == ''
        assert err == ''

        robot.move()
        robot.report()
        out, err = capsys.readouterr()
        assert out == ''
        assert err == ''

        robot.left()
        robot.report()
        out, err = capsys.readouterr()
        assert out == ''
        assert err == ''

        robot.right()
        robot.report()
        out, err = capsys.readouterr()
        assert out == ''
        assert err == ''
