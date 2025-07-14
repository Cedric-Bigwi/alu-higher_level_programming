#!/usr/bin/python3


"""Module for saving a Python object to a file using JSON format."""

import json


def save_to_json_file(my_obj, filename):
    """Writes object to text file using JSON representation."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
