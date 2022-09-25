#!/usr/bin/python3
"""
 prints a square with the character #.

"""


def print_square(size):
    """Print a square with a size.
    size is an int
    size is a float and less than 0
    size is less than 0
    size is equal to 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return (None)

    for row in range(size):
        print('#' * size)
