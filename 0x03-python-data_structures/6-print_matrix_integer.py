#!/usr/b in/python3
def print_matrix_integer(matrix=[[]]):
    a = matrix
    print('\n'.join([' '.join(['{:d}'.format(item) for item in row])
                    for row in a]))