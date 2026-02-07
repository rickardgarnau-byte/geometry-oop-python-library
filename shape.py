"""
Shape module - Abstract base class for geometric 2D shapes.

Provides:
- Common attributes (x, y position)
- Abstract properties for area and perimeter
- Comparison operators based on area and perimeter
- Translation functionality for moving shapes

Source reference:
https://docs.python.org/3/library/abc.html
"""

from abc import ABC, abstractmethod
from utils import validate_number


class Shape(ABC):
    """Abstract base class for 2D shapes."""

    def __init__(self, x: float = 0, y: float = 0):
        """Initialize shape with optional position (x, y)."""
        self.x = x
        self.y = y

    @property
    def x(self) -> float:
        return self._x

    @x.setter
    def x(self, value: float):
        validate_number(value)
        self._x = float(value)

    @property
    def y(self) -> float:
        return self._y

    @y.setter
    def y(self, value: float):
        validate_number(value)
        self._y = float(value)

    """Abstract properties"""
    @property
    @abstractmethod
    def area(self) -> float:
        """Return the area of the shape."""
        pass

    @property
    @abstractmethod
    def perimeter(self) -> float:
        """Return the perimeter of the shape."""
        pass

    """Comparison operators"""
    def __eq__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        return self.area == other.area and self.perimeter == other.perimeter

    def __lt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        if self.area != other.area:
            return self.area < other.area
        return self.perimeter < other.perimeter

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        if not isinstance(other, Shape):
            return NotImplemented
        if self.area != other.area:
            return self.area > other.area
        return self.perimeter > other.perimeter

    def __ge__(self, other):
        return self == other or self > other

    """Utility methods"""
    def translate(self, dx: float, dy: float) -> None:
        """Move the shape by dx and dy."""
        validate_number(dx)
        validate_number(dy)
        self.x += dx
        self.y += dy

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __str__(self) -> str:
        return f"{self.__class__.__name__} at position ({self.x}, {self.y})"
