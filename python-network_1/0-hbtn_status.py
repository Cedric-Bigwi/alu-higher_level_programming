#!/usr/bin/python3
"""This module fetches the status from a URL using urllib and displays response details."""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen("http://0.0.0.0:5050/status") as response:
        body = response.read()
        print("Body response:")
        print("\t- type:", type(body))
        print("\t- content:", body)
        print("\t- utf8 content:", body.decode("utf-8"))
