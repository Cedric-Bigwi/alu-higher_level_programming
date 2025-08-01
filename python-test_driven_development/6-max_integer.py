#!/usr/bin/python3
"""
Module to find the max integer in a list
"""

def max_integer(list=[]):
    """Returns max integer in list or None if empty"""
    if len(list) == 0:
        return None
    result = list[0]
    for i in list:
        if i > result:
            result = i
    return result
