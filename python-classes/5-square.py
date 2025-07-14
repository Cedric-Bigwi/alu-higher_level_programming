#!/usr/bin/python3
"""Module for Square with print method."""

class Square:
    """Defines a square that can be printed."""

    def __init__(self, size=0):
        """Initialize square with validated size."""
        self.size = size

    @property
    def size(self):
        """Retrieve size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return area of square."""
        return self.__size ** 2

    def my_print(self):
        """Print square using # character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)

