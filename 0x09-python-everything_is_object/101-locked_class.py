#!/usr/bin/python3
class LockedClass:
    """A locked class that prevent the user from dynamically creating new
    instance attribute except if its called first_name"""

 def __setattr__(self, attribute, value):
        if attribute == "first_name":
            self.__dict__[attribute] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + attribute + "'")

