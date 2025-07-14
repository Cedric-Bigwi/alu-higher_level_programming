#!/usr/bin/python3


"""Module for writing a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a UTF-8 text file and returns char count."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
