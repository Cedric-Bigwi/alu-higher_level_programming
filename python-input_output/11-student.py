#!/usr/bin/python3


class Student:
    """Defines a student with methods for serialization and reloading."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dict of selected attributes if list is given, else all."""
        if isinstance(attrs, list):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces attributes of Student from dictionary."""
        for key, value in json.items():
            setattr(self, key, value)

