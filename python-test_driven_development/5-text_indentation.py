#!/usr/bin/python3
"""A function that prints text with 2 new lines after each '.', '?' and ':'"""


def text_indentation(text):
    """Prints a text with 2 new lines after '.', '?' and ':'"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    i = 0
    length = len(text)

    while i < length:
        print_char = text[i]
        print(print_char, end='')

        if print_char in delimiters:
            print('\n')
            i += 1
            # Skip following spaces
            while i < length and text[i] == ' ':
                i += 1
            continue
        i += 1
