import pytest
from rover_foxbit.entity import Rover, Point


def test_rover_orientation(rover: Rover):
    """Assure orientation must be valid."""
    assert rover.orientation in 'NWSE'


def test_rover_poisition(rover: Rover):
    """Assure rover position is on plateau limits."""
    assert rover.position.x >= rover.plateau.bottom_left.x
    assert rover.position.x <= rover.plateau.top_right.x
    assert rover.position.y >= rover.plateau.bottom_left.y
    assert rover.position.y <= rover.plateau.top_right.y


@pytest.mark.parametrize('initial, expected',
                         [['N', 'W'], ['W', 'S'], ['S', 'E'], ['E', 'N']])
def test_rover_spin_left(rover: Rover, initial, expected):
    """Check rover orientation after a left spin."""
    rover.orientation = initial
    rover.explore('L')
    assert rover.orientation == expected


@pytest.mark.parametrize('initial, expected',
                         [['N', 'E'], ['E', 'S'], ['S', 'W'], ['W', 'N']])
def test_rover_spin_right(rover: Rover, initial, expected):
    """Check rover orientation after a right spin."""
    rover.orientation = initial
    rover.explore('R')
    assert rover.orientation == expected


@pytest.mark.parametrize(
    'orientation, inital, expected',
    [['N', Point(2, 2), Point(2, 3)], ['W', Point(
        2, 2), Point(1, 2)], ['S', Point(2, 2), Point(2, 1)],
     ['E', Point(2, 2), Point(3, 2)]])
def test_rover_move(rover: Rover, orientation, inital, expected):
    """Check rover move according to its orientation."""
    rover.orientation = orientation
    rover.position = inital
    rover.explore('M')
    assert rover.position == expected
