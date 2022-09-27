#!/usr/bin/python3
"""
Function that inserts a line of text to a file.
"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file"""

    with open(filename, "r+", encoding="utf-8") as readFile:
        temp = readFile.readlines()

    count = 0
    with open(filename, "w", encoding="utf-8") as writeFile:
        for lines in temp:
            count += 1
            if search_string in lines:
                temp.insert(count, new_string)
        for lines in temp:
            writeFile.write(lines)
