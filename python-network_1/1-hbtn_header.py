#!/usr/bin/python3
"""Displays the value of X-Request-Id from response header"""
import urllib.request
import sys
"""This script fetches a given URL and displays a formatted response."""

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get("X-Request-Id"))
