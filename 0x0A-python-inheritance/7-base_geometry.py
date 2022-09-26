#!/usr/bin/python3
"""
Defines BaseGeometry that raises an exception area().
"""


class BaseGeometry:
    """A class BaseGeometry"""

    def area(self):
        """that raises an exception"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value"""

        if type(value) != int:
            raise TypeError("[] must be an integer".format(name))
        if 0 >= value:
            raise ValueError("{} must be greater than 0".format(name))
