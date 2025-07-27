#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response."""

from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = parse.urlencode({'email': email}).encode()
    req = request.Request(url, data=data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
