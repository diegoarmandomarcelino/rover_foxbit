from .exceptions import BusyPointError, OutOfBoundsError
from .plateau import Plateau
from .point import Point
from copy import copy

import logging

logger = logging.getLogger(__name__)


class Rover:
    """Rover representation.

    Attributes:
        plateau: the plateau where the rover is placed on.
        position: the point of the plauteau where the rover is placed on.
        orientation: the rover cardinal orientation: N, S, W or E.
    """

    def __init__(self, plateau: Plateau, position: Point, orientation: str):
        """Initialize rover with plateu it is orientation."""
        self.plateau = plateau
        self.position = position
        self.orientation = orientation
        self.plateau.add_busy_point(self.position)

    def explore(self, instructions: str):
        """Rover explore plateau according to given instructions.

        Args:
            instructions: a string with the sequence of instructions for the
            rover to execute.
        """
        for inst in instructions:
            if inst == 'M':
                self.move()
            elif inst == 'L':
                self.spin_left()
            elif inst == 'R':
                self.spin_right()

    def spin_left(self):
        """Change rover orientation with a left spin."""
        if self.orientation == 'N':
            self.orientation = 'W'
        elif self.orientation == 'W':
            self.orientation = 'S'
        elif self.orientation == 'S':
            self.orientation = 'E'
        elif self.orientation == 'E':
            self.orientation = 'N'

    def spin_right(self):
        """Change rover orientation with a right spin."""
        if self.orientation == 'N':
            self.orientation = 'E'
        elif self.orientation == 'E':
            self.orientation = 'S'
        elif self.orientation == 'S':
            self.orientation = 'W'
        elif self.orientation == 'W':
            self.orientation = 'N'

    def move(self, points=1):  # noqa: CCR001
        """Move rover according to its orientation.

        Args:
            points: the amount of points to move.

        Returns:
            None.
        """
        new_position = copy(self.position)
        if self.orientation == 'N':
            new_position.y = self.position.y + points
        elif self.orientation == 'S':
            new_position.y = self.position.y - points
        elif self.orientation == 'E':
            new_position.x = self.position.x + points
        elif self.orientation == 'W':
            new_position.x = self.position.x - points

        try:
            self.plateau.add_busy_point(new_position)
        except OutOfBoundsError:
            logger.warning('rover try to go out of bounds')
        except BusyPointError:
            logger.warning('rover try to go to busy point')
        else:
            self.plateau.remove_busy_point(self.position)
            self.position = new_position
