"""
Sphere module - Represents a 3D sphere.

Provides:
- Radius validation
- Volume, surface area, and great circle circumference calculations
"""

from utils import validate_number
import math


class Sphere:
    """Represents a 3D sphere defined by its radius."""

    def __init__(self, radius: float):
        """Initialize a Sphere with a given radius."""
        self.radius = radius

    @property
    def radius(self) -> float:
        """Get the radius of the sphere."""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """Set the radius with validation."""
        if isinstance(value, bool):
            raise TypeError("Radius must not be a boolean value")
        validate_number(value)
        if value <= 0:
            raise ValueError("Radius must be larger than zero")
        self._radius = float(value)

    """Geometric properties"""
    
    @property
    def surface_area(self) -> float:
        """Return the surface area of the sphere (4πr²)."""
        return 4 * math.pi * (self.radius**2)

    @property
    def volume(self) -> float:
        """Return the volume of the sphere (4/3 πr³)."""
        return (4 / 3) * math.pi * (self.radius**3)

    @property
    def circumference(self) -> float:
        """Return the circumference of the great circle (2πr)."""
        return 2 * math.pi * self.radius

    """Representations"""

    def __repr__(self) -> str:
        return f"Sphere(radius={self.radius})"

    def __str__(self) -> str:
        return (
            f"Sphere with radius={self.radius:.2f}, "
            f"volume={self.volume:.2f}, "
            f"surface_area={self.surface_area:.2f}"
        )

if __name__ == "__main__":
    try:
        r = float(input("Please enter the radius of the sphere: "))
        s = Sphere(r)
        print(f"Volume: {s.volume:.2f}")
        print(f"Surface Area: {s.surface_area:.2f}")
        print(f"Circumference: {s.circumference:.2f}")
    except (ValueError, TypeError) as e:
        print("Error:", e)
