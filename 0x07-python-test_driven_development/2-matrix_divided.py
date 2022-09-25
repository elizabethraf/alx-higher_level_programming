#!/usr/bin/python3
"""
>>> add_integer(1, 2)
3
>>> add_integer('a', 3)
a must be an integer
>>> add_integer(3, 'f')
b must be an integer
>>> add_integer(None)
a must be an integer
"""


def matrix_divided(matrix, div):
    """Divides all elements in the matrix"""
    if type(matrix) != list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    size = None
    for l in matrix:
        if type(l)!= list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size == None:
            size = len(l)
        elif size != len(l):
            raise TypeError("Each row of the matrix must have the same size")
        for a in l:
            if type(a) != int and type(a) != float:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(a / div, 2) for a  in l] for l in matrix]
