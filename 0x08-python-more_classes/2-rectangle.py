#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Example Google style docstrings.
"""


class Rectangle:
    """Defines an empty  rectangle"""

    def __init__(self, width=0, height=0):
        """Initialising data."""
        pass
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """that returns the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """ that returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return self.__width * 2 + self.__height * 2
