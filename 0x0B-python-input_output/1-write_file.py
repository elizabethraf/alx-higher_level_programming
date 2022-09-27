#!/usr/bin/python3
"""
Function that writes a string to a text file(UTF8).

"""


def write_file(filename="", text=""):
    """Defines a string to a text file"""

    try:
        with open(filename, encoding="utf-8") as f:
            f.write(text)
            pass

        return
