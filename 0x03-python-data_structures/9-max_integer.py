#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        large = my_list[0]
    for idx in my_list:
        if idx > large:
            large = idx
        return ((min(my_list, key=lambda i: -i)) if my_list else None)
