#!/usr/bin/python3
"""
Define Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializss the square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """information of the square"""
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x,
                                                         self.y, self.width)

    def update(self, *args, **kwargs):
        """update attributes"""
        if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"

        else:
            for key, values in kwargs.items():
                setattr(self, key, values)

           def to_dictionary(self):
        """difine dictionary"""
        dictionary = {}
        for index in ["id", "size", "x", "y"]:
            dictionary[index] = getattr(self, index)
        return dictionary
