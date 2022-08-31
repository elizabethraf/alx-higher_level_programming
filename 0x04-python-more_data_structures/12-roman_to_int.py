#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    number = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    float = 0
    for j in range(len(roman_string)):
        value = number[roman_string[j]]
        if j + 1 < len(roman_string) and number[roman_string[j + 1]] > value:
            float -= value
        else:
            float += value
    return float
