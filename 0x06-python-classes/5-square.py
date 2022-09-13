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

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        return: None
        """
        self.__size = size

        if type(self.__size) != int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        self.area = self.__size ** 2

        return (self.area)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        """property setter of __size
        Args:
            vaue (int): The size of the new square
        return: None
        """
        self.__size = value

        if type(value) != int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")

    def my_print(self):
        """prints the square
        return: None
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("".join(["#" for j in range(self.__size)]))
