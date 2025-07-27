#!/usr/bin/python3
"""Uses GitHub API to fetch user ID"""
import requests
import sys
res = requests.get("https://api.github.com/user", auth=(sys.argv[1], sys.argv[2]))
print(res.json().get("id"))
