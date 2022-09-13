#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The size of a square is crucial for a square, many things depend of it (area
computation, etc.).


Attributes:
    size (int): The size of the new square.
"""


class Square:
    """Defines a square."""

    def __init__(self, size):
        """Initialize a new Square.


        Args:
            size (int): The size of the new square.

        return: None
        """
        self.__size = size
