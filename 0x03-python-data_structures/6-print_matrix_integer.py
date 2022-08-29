#!/usr/b in/python3
def print_matrix_integer(matrix=[[]]):
    for a in matrix:
        print(' '.join("{:d}".format(i) for i in a))
