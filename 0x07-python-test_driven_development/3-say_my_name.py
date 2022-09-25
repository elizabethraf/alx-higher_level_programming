#!/usr/bin/python3
"""
 print My name is <first name> <last name>
 first_name and last_name must be strings otherwise
"""


def say_my_name(first_name, last_name=""):
    """ Print "My name is <first name> <last name>"
    first_name must be a string
    last_name must be a string
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))
