#!/usr/bin/python3
"""Fetches and displays status from the specified URL using requests."""

import requests

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    r = requests.get(url)
    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")
