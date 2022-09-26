#!/usr/bin/python3
"""
Defines MyInt that inherits from int.
"""


class MyInt(int):
    """MyInt inherits from int."""

    def __eq__(self, value):
        """method equals"""

        return super().__ne__(value)

    def __ne__(self, value):
        """method is not equal."""

        if(self.real != value):
            return False
        return True
