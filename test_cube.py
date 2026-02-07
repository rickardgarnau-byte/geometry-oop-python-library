"""
Test suite for the Cube class.

Sources:
- http://pythonfiddle.com/python-program-to-write-a-cube-class/
- https://github.com/Db-Lau/python_code_along_DE25/tree/main/exercises/tdd_exercise
"""

from pytest import raises
from cube import Cube
import math


def test_valid_init():
    cube = Cube(side=8)
    assert cube.side == 8


def test_negative_side():
    with raises(ValueError):
        Cube(side=-1)


def test_string_side():
    with raises(TypeError):
        Cube(side="8")


def test_boolean_side():
    with raises(TypeError):
        Cube(side=True)


def test_set_side_valid():
    cube = Cube(side=4)
    cube.side = 5
    assert cube.side == 5


def test_set_side_negative():
    cube = Cube(side=4)
    with raises(ValueError):
        cube.side = -2


def test_set_side_string():
    cube = Cube(side=4)
    with raises(TypeError):
        cube.side = "a"


def test_float_side_calculations():
    cube = Cube(side=2.5)
    assert math.isclose(cube.volume, 2.5 ** 3)
    assert math.isclose(cube.surface_area, 6 * 2.5 ** 2)


def test_volume_property():
    cube = Cube(side=3)
    assert math.isclose(cube.volume, 27)


def test_surface_area_property():
    cube = Cube(side=2)
    assert math.isclose(cube.surface_area, 24)


def test_perimeter_property():
    cube = Cube(side=1.5)
    assert math.isclose(cube.perimeter, 18)
