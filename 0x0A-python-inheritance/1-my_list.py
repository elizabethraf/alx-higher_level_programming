#!/usr/bin/python3
"""
Defines MyList that inherits from list

"""


class MyList(list):
    """
    Defines List
    """

    def print_sorted(self):
        """Print list.
        """

        print(list(self))

    def __init__(self):
        """initialise object"""
        super().__init__()
