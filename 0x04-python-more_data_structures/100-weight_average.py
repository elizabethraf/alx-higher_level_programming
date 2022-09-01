#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        count = 0
        value = 0
        for float in my_list:
            count += (float[0] * float[1])
            value += float[1]
        return (count / value)
    return 0
