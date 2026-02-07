from shape import Shape
from utils import validate_number
import math


class Rectangle(Shape):
    """
    Represents a rectangle shape inheriting from Shape.

    Attributes:
        x (float): The x-coordinate of the top-left corner.
        y (float): The y-coordinate of the top-left corner.
        width (float): Rectangle width (must be positive).
        height (float): Rectangle height (must be positive).
    """

    def __init__(self, x: float = 0, y: float = 0, width: float = 1, height: float = 1):
        super().__init__(x, y)
        self.width = width
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float):
        validate_number(value)
        if value < 0:
            raise ValueError("The width cannot be negative")
        self._width = float(value)

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float):
        validate_number(value)
        if value < 0:
            raise ValueError("The height cannot be negative")
        self._height = float(value)

    @property
    def area(self) -> float:
        """Return the area of the rectangle"""
        return self.width * self.height

    @property
    def perimeter(self) -> float:
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    @property
    def is_square(self) -> bool:
        """Check if the rectangle is a square."""
        return math.isclose(self.width, self.height)

    def __repr__(self) -> str:
        return (
            f"Rectangle(x={self.x}, y={self.y}, "
            f"width={self.width}, height={self.height})"
        )

    def __str__(self) -> str:
        return (
            f"Rectangle (w={self.width}, h={self.height}) at ({self.x}, {self.y}). "
            f"Area: {self.area:.2f}, Perimeter: {self.perimeter:.2f}"
        )


if __name__ == "__main__":
    r = Rectangle(width=4, height=6)
    print(r)
    print("Is square?", r.is_square)
    r.translate(5, 2)
    print("Moved to:", (r.x, r.y))