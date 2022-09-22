#!/usr/bin/python3
class LockedClass:
    """A locked class that prevent the user from dynamically creating new
    instance attribute except if its called first_name"""

    __slots__ = ['first_name']
