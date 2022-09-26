#!/usr/bin/python3
"""
Defines class BaseGeometry and subclass Rectangle.

"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines rectangle"""

    def __init__(self, width, height):
        """initialise the rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width
