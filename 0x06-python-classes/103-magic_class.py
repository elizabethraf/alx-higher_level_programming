#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
The size of a square is crucial for a square, many things depend of it (area
computation, etc.).
Attributes:
    size (int): The size of the new circle.
"""
import math


class MagicClass:
    """Define a Magic Class"""
    def __init__(self, radius=0):
        """Initializes  Magic Class"""
        self__radius = 0

        if type(radius) != int and type(radius) != float:
            raise TypeError('radius must be a number')
        self__radius = radius

    def area(self):
        self.area = self__radius ** 2

        return (self__radius ** 2) * math.pi

    def circumference(self):
        self.circumference = self_radious ** 2

        return (2 * math.pi * self__radius)
