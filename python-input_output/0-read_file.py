#!/usr/bin/python3


"""Module for reading and printing the contents of a file."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")

