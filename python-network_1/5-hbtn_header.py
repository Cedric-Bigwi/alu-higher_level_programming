#!/usr/bin/python3
"""Displays X-Request-Id from header using requests"""
import requests
import sys
res = requests.get(sys.argv[1])
print(res.headers.get("X-Request-Id"))
