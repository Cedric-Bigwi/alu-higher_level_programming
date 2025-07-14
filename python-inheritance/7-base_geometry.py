#!/usr/bin/python3
"""Module 7-base_geometry.py"""


class BaseGeometry:
    """Base class with area and validator."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
