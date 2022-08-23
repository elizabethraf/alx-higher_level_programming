#!/usr/bin/python3
def uppercase(str):
    for b in str:
        _i = ord(b)
        if _i >= 97 and _i <= 122:
            char = chr(_i - 32)
        else:
            char = b
        print("{:s}".format(char), end="")
    print('')
