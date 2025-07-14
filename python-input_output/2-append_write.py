#!/usr/bin/python3


def append_write(filename="", text=""):
    """Appends string to end of UTF-8 text file and returns char count."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

