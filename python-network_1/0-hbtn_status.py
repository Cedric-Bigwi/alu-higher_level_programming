#!/usr/bin/python3
"""Fetches and displays the status from the specified URL using urllib."""

from urllib import request

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    with request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
