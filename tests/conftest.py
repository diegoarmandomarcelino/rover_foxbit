import pytest

from . import factories

from rover_foxbit import entity


@pytest.fixture
def rover() -> entity.Rover:
    """Create a random rover instance."""
    return factories.RoverFactory()


@pytest.fixture
def plateau() -> entity.Plateau:
    """Create a random plateau instance."""
    return factories.PlateauFactory()
