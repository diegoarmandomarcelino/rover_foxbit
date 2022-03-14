import pytest
from rover_foxbit.entity import Plateau, Point
from rover_foxbit.entity.exceptions import OutOfBoundsError, BusyPointError


def test_plateau_initialize_with_no_busy_points(plateau: Plateau):
    """Check just initialized plateau has no busy points."""
    assert plateau.busy_points == []


def test_point_added_to_busy_points(plateau: Plateau):
    """Check a point is added to busy points."""
    point = Point(0, 0)
    plateau.add_busy_point(point)
    assert point in plateau.busy_points


def test_point_removed_to_busy_points(plateau: Plateau):
    """Check point is removed from busy points."""
    point = Point(0, 0)
    plateau.add_busy_point(point)
    plateau.remove_busy_point(point)
    assert point not in plateau.busy_points


def test_remove_unexists_to_busy_points_no_error(plateau: Plateau):
    """Check no exception when try to remove non existing busy point."""
    point = Point(0, 0)
    plateau.remove_busy_point(point)
    assert point not in plateau.busy_points


@pytest.mark.parametrize('x, y', [[-1, 0], [0, -1], [9999999, 0], [0, 9999999]])
def test_out_of_bounds_exception(plateau: Plateau, x, y):
    """Check out of bounds exception correctly raised."""
    point = Point(x, y)
    with pytest.raises(OutOfBoundsError) as e:
        plateau.add_busy_point(point)
    assert str(point) in str(e)


def test_busy_point_exception(plateau: Plateau):
    """Check busy point exception correctly raised."""
    point = Point(0, 0)
    plateau.add_busy_point(point)
    with pytest.raises(BusyPointError) as e:
        plateau.add_busy_point(point)
    assert str(point) in str(e)
