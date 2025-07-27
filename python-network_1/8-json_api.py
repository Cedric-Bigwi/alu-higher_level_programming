#!/usr/bin/python3
"""POST with a letter as query param to a JSON API"""
import requests
import sys
q = "" if len(sys.argv) == 1 else sys.argv[1]
res = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
try:
    js = res.json()
    if js:
        print("[{}] {}".format(js.get("id"), js.get("name")))
    else:
        print("No result")
except ValueError:
    print("Not a valid JSON")
