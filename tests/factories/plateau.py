from factory import Factory, SubFactory
from rover_foxbit.entity.plateau import Plateau
from .point import PointFactory


class PlateauFactory(Factory):
    """Factory object for plateau."""

    class Meta:
        """Meta info."""

        model = Plateau

    top_right = SubFactory(PointFactory)
