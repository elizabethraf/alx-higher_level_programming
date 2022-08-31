#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        col = list(map(lambda j: j ** 2, row))
        new_matrix.append(col)
    return (new_matrix)
