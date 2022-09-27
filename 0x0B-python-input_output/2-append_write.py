#!/usr/bin/python3
"""
Function that appends a string at the end of text file(UTF8).

"""


def append_write(filename="", text=""):
    """Defines function that append a string"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
