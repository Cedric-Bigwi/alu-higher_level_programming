#!/usr/bin/python3
"""Sends a POST request to search for a user and displays the id and name or an error message."""

import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    r = requests.post("http://0.0.0.0:5000/search_user", data={'q': q})
    try:
        data = r.json()
        if data:
            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
