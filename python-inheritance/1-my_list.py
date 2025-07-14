#!/usr/bin/python3
"""Module 1-my_list.py"""
class MyList(list):
    """Custom list class with sorted print."""
    def print_sorted(self):
        print(sorted(self))
