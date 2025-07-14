#!/usr/bin/python3


"""Script that adds all arguments to a Python list and saves them in a file."""

import sys
import os
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file

filename = "add_item.json"

if os.path.exists(filename):
    try:
        data = load_from_json_file(filename)
    except Exception:
        data = []
else:
    data = []

data.extend(sys.argv[1:])
save_to_json_file(data, filename)
