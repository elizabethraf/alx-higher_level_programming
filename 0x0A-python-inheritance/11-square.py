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

    def area(self):
        """Calculates area of rectangle."""

        return self.__width * self.__height

    def __str__(self):
        """Description of rectangle."""

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """Class Square inherits from Rectangle."""

    def __init__(self, size):
        """initialise the size of the square."""

        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of  Square"""
        return self.__size ** 2

    def __str__(self):
        """informal string  of a square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
