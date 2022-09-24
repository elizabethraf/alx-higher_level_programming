#!/usr/bin/pyon3
"""
>>> my_function(2, 3)
6
>>> my_function('a', 3)
'aaa'
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
