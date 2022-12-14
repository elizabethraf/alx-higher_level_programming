#!/usr/bin/python3
"""
Class Rectangle inherits from Base

"""

from models.base import Base


class Rectangle(Base):
    """Defines an empty  rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialising a rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for the width"""
        return self.__width

    @property
    def height(self):
        """getter for the height"""
        return self.__height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @width.setter
    def width(self, value):
        """setter for the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """setter for the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """setter of x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """setter of y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """getter for the area"""
        return self.__width * self.__height

    def display(self):
        """Define display"""
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for a in range(self.__height)))

    def __str__(self):
        """information of the shape"""
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.__x,
                                                                 self.__y,
                                                                 self.__width,
                                                                 self.__height)

    def update(self, *args, **kwargs):
        """updates attributes"""
        if len(args):
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

        def to_dictionary(self):
            """Define dictionary"""
            dictionary = {}
            for index in ["id", "width", "height", "x", "y"]:
                dictionary[index] = getattr(self, index)
                return dictionary
