#!/usr/bin/python3


"""Module for returning dictionary representation of object for JSON serialization."""


def class_to_json(obj):
    """Returns dictionary description for JSON serialization."""
    return obj.__dict__
