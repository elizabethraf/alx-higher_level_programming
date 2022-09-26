#!/usr/bin/python3
"""
Defines new  add_attribute

"""


def add_attribute(a_class, name, value):
    """Add new attribute ."""

    cannot_add = {int, str, float, list, dict, tuple, frozenset, type, object}

    if type(a_class) in cannot_add:
        raise TypeError("can't add new attribute")

    setattr(a_class, name, value)
