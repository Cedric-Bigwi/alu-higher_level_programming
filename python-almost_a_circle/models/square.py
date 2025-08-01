#!/usr/bin/python3
"""This module defines a Square class inheriting from Rectangle."""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Represents a square shape with equal width and height."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize square with size, x, y, and optional id."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square, adjusting width and height."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update attributes using args or kwargs."""
        attr_order = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(attr_order):
                    setattr(self, attr_order[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Return dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
