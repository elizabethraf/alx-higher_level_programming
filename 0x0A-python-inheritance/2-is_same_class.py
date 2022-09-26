#!/usr/bin/python3
"""
Defines is_same_class(obj, a_class).

"""


def is_same_class(obj, a_class):
    """It return True if object is an instance of class, otherwise false"""

    return (type(obj) == a_class)
