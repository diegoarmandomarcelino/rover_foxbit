from random import randint

from factory import Factory, SubFactory, lazy_attribute
from factory.fuzzy import FuzzyChoice

from rover_foxbit.entity import Rover
from rover_foxbit.entity.point import Point
from .plateau import PlateauFactory


class RoverFactory(Factory):
    """Factory object for rover."""

    class Meta:
        """Meta info."""

        model = Rover

    plateau = SubFactory(PlateauFactory)
    orientation = FuzzyChoice('NWSE')

    @lazy_attribute
    def position(self):
        """Create a initial position inside plateau limits."""
        x = randint(self.plateau.bottom_left.x, self.plateau.top_right.x)
        y = randint(self.plateau.bottom_left.y, self.plateau.top_right.y)
        return Point(x, y)
