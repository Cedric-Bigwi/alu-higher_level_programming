#!/usr/bin/python3
"""Handles HTTP errors and displays the response body or error code."""

from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
