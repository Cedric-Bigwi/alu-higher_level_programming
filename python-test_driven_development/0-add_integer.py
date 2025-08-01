#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (cast to int).

    Raises:
        TypeError: if either a or b is not an int or float
        ValueError: if a or b is NaN or infinite

    Returns:
        The sum as an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if (
        a != a or b != b or
        a in [float("inf"), float("-inf")] or
        b in [float("inf"), float("-inf")]
    ):
        raise ValueError("cannot convert float NaN or inf to integer")

    return int(a) + int(b)
