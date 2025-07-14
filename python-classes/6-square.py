#!/usr/bin/python3
"""Module for Square with position attribute."""


class Square:
    """Defines a square with position and size."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize square with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position of square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(i, int) and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of square."""
        return self.__size ** 2

    def my_print(self):
        """Print square with # using position offset."""
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
