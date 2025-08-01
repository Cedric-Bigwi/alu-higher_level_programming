#!/usr/bin/python3
"""
Module for text_indentation function
Prints text with two new lines after ., ?, and :
"""

def text_indentation(text):
    """Prints text with indentation"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:":
        text = text.replace(delim, delim + "\n\n")
    lines = [line.strip() for line in text.split("\n")]
    for line in lines:
        if line:
            print(line)
