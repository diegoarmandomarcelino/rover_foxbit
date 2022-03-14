from rover_foxbit.entity.point import Point
from factory import Factory
from factory.fuzzy import FuzzyInteger


class PointFactory(Factory):
    """Factory object for point."""

    class Meta:
        """Meta info."""

        model = Point

    x = FuzzyInteger(5, 100)
    y = FuzzyInteger(5, 100)
