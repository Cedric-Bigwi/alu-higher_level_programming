#!/usr/bin/python3
"""Fetches status using requests"""
import requests
res = requests.get("https://alu-intranet.hbtn.io/status")
print("Body response:")
print("\t- type:", type(res.text))
print("\t- content:", res.text)
