"""
Test suite for the Sphere class.

Sources:
- https://www.w3resource.com/python-exercises/math/python-math-exercise-6.php
- cube.py used as a structural template
"""

from pytest import raises
from sphere import Sphere
import math


def test_valid_init():
    sphere = Sphere(radius=8)
    assert sphere.radius == 8


def test_init_with_negative_radius():
    with raises(ValueError):
        Sphere(radius=-1)


def test_init_with_string_radius():
    with raises(TypeError):
        Sphere(radius="8")


def test_init_with_boolean_radius():
    with raises(TypeError):
        Sphere(radius=True)


def test_set_radius_valid():
    sphere = Sphere(radius=4)
    sphere.radius = 5
    assert sphere.radius == 5


def test_set_radius_to_negative_value():
    sphere = Sphere(radius=4)
    with raises(ValueError):
        sphere.radius = -2


def test_set_radius_to_string():
    sphere = Sphere(radius=4)
    with raises(TypeError):
        sphere.radius = "a"


def test_float_radius():
    sphere = Sphere(radius=5.5)
    assert math.isclose(sphere.volume, (4 / 3) * math.pi * 5.5**3)
    assert math.isclose(sphere.surface_area, 4 * math.pi * 5.5**2)


def test_volume_property():
    sphere = Sphere(radius=3)
    assert math.isclose(sphere.volume, (4 / 3) * math.pi * 3**3)


def test_surface_area_property():
    sphere = Sphere(radius=2)
    assert math.isclose(sphere.surface_area, 4 * math.pi * 2**2)


def test_circumference_property():
    sphere = Sphere(radius=1.5)
    assert math.isclose(sphere.circumference, 2 * math.pi * 1.5)
