#!/usr/bin/python3
"""Displays error code if >= 400"""
import requests
import sys
res = requests.get(sys.argv[1])
if res.status_code >= 400:
    print("Error code:", res.status_code)
else:
    print(res.text)
