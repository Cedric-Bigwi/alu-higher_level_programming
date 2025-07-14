#!/usr/bin/python3
"""Module 4-inherits_from.py"""


def inherits_from(obj, a_class):
    """Check if object inherits from class (not direct match)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
