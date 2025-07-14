#!/usr/bin/python3


"""Module for appending a string to the end of a text file."""


def append_write(filename="", text=""):
    """Appends string to end of UTF-8 text file and returns char count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

