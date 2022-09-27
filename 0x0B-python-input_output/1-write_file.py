#!/usr/bin/python3
"""
Function that writes a string to a text file(UTF8).

"""


def write_file(filename="", text=""):
    """Defines a string to a text file"""

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
