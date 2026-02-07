from shape import Shape
from utils import validate_number
import math


class Circle(Shape):
    """
    Represents a circle shape inheriting from Shape.

    Attributes:
        x (float): X-coordinate of the circle center.
        y (float): Y-coordinate of the circle center.
        radius (float): Circle radius (must be positive).
    """

    def __init__(self, x: float = 0, y: float = 0, radius: float = 1):
        super().__init__(x, y)
        self.radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        validate_number(value)
        if value < 0:
            raise ValueError("The radius cannot be negative")
        self._radius = float(value)

    @property
    def area(self) -> float:
        """Return the area of the circle (πr²)."""
        return math.pi * self.radius**2

    @property
    def perimeter(self) -> float:
        """Return the circumference of the circle (2πr)."""
        return 2 * math.pi * self.radius

    @property
    def is_unit_circle(self) -> bool:
        """
        Check if the circle is a unit circle. This is taken from 'LLM'.
        A unit circle has radius = 1 and center at (0, 0).
        """
        return (
            math.isclose(self.radius, 1)
            and math.isclose(self.x, 0)
            and math.isclose(self.y, 0)
        )

    def __repr__(self) -> str:
        return f"Circle(x={self.x}, y={self.y}, radius={self.radius})"

    def __str__(self) -> str:
        return (
            f"Circle at ({self.x}, {self.y}) with radius {self.radius}. "
            f"Area: {self.area:.2f}, Perimeter: {self.perimeter:.2f}"
        )


if __name__ == "__main__":
    c = Circle(radius=5)
    print(c)
    print("Is unit circle?", c.is_unit_circle)
    c.translate(3, -1)
    print("Moved to:", (c.x, c.y))
