#!/usr/bin/pyon3
"""
>>> add_integer(1, 2)
3
>>> add_integer('a', 3)
a must be an integer
>>> add_integer(3, 'f')
b must be an integer
>>> add_integer(None)
a must be an integer
"""

def add_integer(a, b=98):
    """Define an integers"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return (a + b)
