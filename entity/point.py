from dataclasses import dataclass


@dataclass
class Point:
    """Represents a point by its X and Y coordinates."""

    x: int
    y: int

    def __eq__(self, other) -> bool:
        """Check whether an other point is equal or not."""
        return self.x == other.x and self.y == other.y

    def __str__(self) -> str:
        """Return string representation."""
        return f'Point[x:{self.x}|y:{self.y}]'
