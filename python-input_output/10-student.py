#!/usr/bin/python3


"""Module defining a Student class with optional attribute filtering for JSON."""


class Student:
    """Defines a student with public attributes and optional filtering."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict of selected attributes if list is given, else all."""
        if isinstance(attrs, list):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

