#!/usr/bin/python3
"""This module defines a Rectangle class that inherits from Base."""
from models.base import Base

class Rectangle(Base):
    """Defines a rectangle with width, height, x, y and id."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle instance and validate input."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__validate_integer("width", value, greater_than_zero=True)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__validate_integer("height", value, greater_than_zero=True)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__validate_integer("y", value)
        self.__y = value

    def __validate_integer(self, name, value, greater_than_zero=False):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if greater_than_zero and value <= 0:
            raise ValueError(f"{name} must be > 0")
        elif not greater_than_zero and value < 0:
            raise ValueError(f"{name} must be >= 0")

    def area(self):
        """Returns the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Prints the rectangle using '#' character, considering x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Returns a custom string representation of the Rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Updates attributes using args or kwargs."""
        attr_order = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(attr_order):
                    setattr(self, attr_order[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary representation of the Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
