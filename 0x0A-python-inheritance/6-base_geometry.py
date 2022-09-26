#!/usr/bin/python3
"""
Defines BaseGeometry that raises an exception area().

"""


class BaseGeometry:
    """A class BaseGeometry"""

    def area(self):
        """that raises an exception"""

        raise Exception("area() is not implemented")
