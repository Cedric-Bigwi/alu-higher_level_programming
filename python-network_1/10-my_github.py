#!/usr/bin/python3
"""Uses GitHub API to display user id with Basic Authentication."""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    r = requests.get("https://api.github.com/user", auth=(username, token))
    if r.status_code == 200:
        print(r.json().get('id'))
    else:
        print("None")
