#!/usr/bin/python3
"""Sends a POST request with an email using requests"""
import requests
import sys
res = requests.post(sys.argv[1], data={"email": sys.argv[2]})
print(res.text)
