#!/usr/bin/python3
"""
Class Rectangle inherits from Base
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines an empty  square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialising a sqaure"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.size = size

    @property
    def size(self):
        """getter for the width"""
        return self.__width

    @property
    def size(self):
        """getter for the height"""
        return self.__height

    @size.setter
    def size(self, value):
        """Size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updating the size of the Square"""
        if len(kwargs) is not 0:
            for k, v in kwargs.items():
                setattr(self, k, v)
        elif len(args) is not 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            print()

    def to_dictionary(self):
        """Define Dictionery"""
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}

    def __str__(self):
        """String representation"""

        return '[Square] ({}) {}/{} - {}'.format(self.id,
                                                 self.x, self.y, self.size)
