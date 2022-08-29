#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == 0:
        return (None)
    large = my_list[0]
    for idx in my_list:
        if idx > large:
            large = idx
    return (large)
    return (None)
