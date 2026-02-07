"""
Cube module - Represents a 3D cube shape.

Provides:
- Side length validation
- Volume, surface area, and total edge length calculations
"""

from utils import validate_number


class Cube:
    """Represents a cube defined by the length of one side."""

    def __init__(self, side: float):
        """Initialize a new Cube instance."""
        self.side = side

    @property
    def side(self) -> float:
        """Get the side length of the cube."""
        return self._side

    @side.setter
    def side(self, value: float):
        """Set the side length with validation."""
        if isinstance(value, bool):
            raise TypeError("Side must not be a boolean value")
        validate_number(value)
        if value <= 0:
            raise ValueError("Side must be larger than zero")
        self._side = float(value)

    """Geometric properties"""
    
    @property
    def volume(self) -> float:
        """Return the volume of the cube (side³)."""
        return self.side**3

    @property
    def surface_area(self) -> float:
        """Return the surface area of the cube (6 × side²)."""
        return 6 * self.side**2

    @property
    def perimeter(self) -> float:
        """Return the total edge length (12 × side)."""
        return 12 * self.side

    """Representations"""

    def __repr__(self) -> str:
        return f"Cube(side={self.side})"

    def __str__(self) -> str:
        return (
            f"Cube with side={self.side:.2f}, "
            f"volume={self.volume:.2f}, "
            f"surface_area={self.surface_area:.2f}"
        )


if __name__ == "__main__":
    try:
        s = float(input("Please enter the side length of the cube: "))
        c = Cube(s)
        print(f"Volume: {c.volume:.2f}")
        print(f"Surface Area: {c.surface_area:.2f}")
        print(f"Total Edge Length: {c.perimeter:.2f}")
    except (ValueError, TypeError) as e:
        print("Error:", e)
