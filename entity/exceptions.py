from .point import Point


class OutOfBoundsError(ValueError):
    """Out of plateau bounds error."""

    def __init__(self, point: Point, *args, **kwargs) -> None:
        """Initialize exception."""
        message = f'{point} is out of bounds of plateau'
        super().__init__(message, *args, **kwargs)


class BusyPointError(ValueError):
    """Plateau busy point error."""

    def __init__(self, point: Point, *args, **kwargs) -> None:
        """Initialize exception."""
        message = f'{point} is already busy'
        super().__init__(message, *args, **kwargs)
