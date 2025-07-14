#!/usr/bin/python3


"""Module for converting Python objects to JSON string."""

import json


def to_json_string(my_obj):
    """Returns JSON string representation of an object."""
    return json.dumps(my_obj)
