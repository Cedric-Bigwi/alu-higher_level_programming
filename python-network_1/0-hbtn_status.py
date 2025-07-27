#!/usr/bin/python3
"""Fetches http://0.0.0.0:5050/status and prints formatted response"""
import urllib.request
with urllib.request.urlopen("http://0.0.0.0:5050/status") as response:
    body = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
