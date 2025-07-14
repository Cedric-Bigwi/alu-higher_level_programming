#!/usr/bin/python3


def class_to_json(obj):
    """Returns dictionary description for JSON serialization."""
    return obj.__dict__

