#!/usr/bin/python3
"""
Defines objects of instance

"""


def inherits_from(obj, a_class):
    """It return True if object is an instance of class, otherwise false"""

    return(type(obj) != a_class and issubclass(type(obj), a_class))
