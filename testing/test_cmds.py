import pytest
from toy_robot import command_parser
from toy_robot.command_parser import CommandParser, InputError


class TestsCommandParser:
    def test_place_cmd(self):
        c = CommandParser('PLACE 1,2,NORTH\n')
        assert c.cmd == 'PLACE'
        assert c.coordinates[0] == 1
        assert c.coordinates[1] == 2
        assert c.direction == 'NORTH'


    def test_report_cmd(self):
        c = CommandParser('REPORT\n')
        assert c.cmd == 'REPORT'
        assert c.coordinates == (None, None)
        assert c.direction == None


    def test_move_cmd(self):
        c = CommandParser('MOVE\n')
        assert c.cmd == 'MOVE'
        assert c.coordinates == (None, None)
        assert c.direction == None


    def test_left_cmd(self):
        c = CommandParser('LEFT\n')
        assert c.cmd == 'LEFT'
        assert c.coordinates == (None, None)
        assert c.direction == None


    def test_right_cmd(self):
        c = CommandParser('RIGHT\n')
        assert c.cmd == 'RIGHT'
        assert c.coordinates == (None, None)
        assert c.direction == None

    def test_wrong_cmd(self):
        with pytest.raises(InputError):
            c = CommandParser('JUMP\n')


    def test_place_no_coords(self):
        with pytest.raises(InputError):
            c = CommandParser('PLACE\n')


    def test_wrong_directions(self):
        with pytest.raises(InputError):
            c = CommandParser('PLACE 0,0,NORTHEAST\n')


    def test_wrong_x(self):
        with pytest.raises(InputError):
            c = CommandParser('PLACE X,0,WEST\n')


    def test_wrong_y(self):
        with pytest.raises(InputError):
            c =  CommandParser('PLACE 0,Y,WEST\n')
