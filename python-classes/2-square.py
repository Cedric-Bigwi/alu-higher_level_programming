#!/usr/bin/python3
"""Module for Square with size validation."""

class Square:
    """Defines a square with size validation."""

    def __init__(self, size=0):
        """Initialize square and validate size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

