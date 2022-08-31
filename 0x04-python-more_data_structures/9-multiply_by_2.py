#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = dict(a_dictionary)
    for key, value in result.items():
        result[key] = value * 2
    return(result)
