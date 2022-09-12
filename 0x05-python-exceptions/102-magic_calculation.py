#!/usr/bin/python3
def magic_calculation(a, b):
    count = 0
    for y in range(4, 6):
        try:
            if a < b:
                raise Exception("Too far")
            else:
                count += (a ** b) / y
         except:
               count = b + a
               break
         return (count)
