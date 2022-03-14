import logging
from dataclasses import dataclass, field
from typing import List
from contextlib import suppress

from .exceptions import BusyPointError, OutOfBoundsError

from .point import Point

logger = logging.getLogger(__name__)


@dataclass
class Plateau:
    """Represents a plateu using 2 points, a top right and a bottom left."""

    top_right: Point
    bottom_left: Point = Point(0, 0)
    busy_points: List[Point] = field(default_factory=list)

    def add_busy_point(self, point: Point):
        """Add a point to busy points of the plateau.

        Args:
            point: the point to be added.

        Raises:
            BusyPointError: when point is already busy.
            OutOfBoundsError: when point is out of the plateau bounds.
        """
        if point in self.busy_points:
            raise BusyPointError(point)
        if self.bottom_left.x > point.x or point.x > self.top_right.x:
            raise OutOfBoundsError(point)
        if self.bottom_left.y > point.y or point.y > self.top_right.y:
            raise OutOfBoundsError(point)
        self.busy_points.append(point)
        logger.debug(self.busy_points)

    def remove_busy_point(self, point: Point):
        """Remove point from busy points.

        Args:
            point: the point to be removed.
        """
        with suppress(ValueError):
            self.busy_points.remove(point)
