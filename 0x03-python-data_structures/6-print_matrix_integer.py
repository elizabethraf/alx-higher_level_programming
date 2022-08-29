#!/usr/b in/python3
def print_matrix_integer(matrix=[[]]):
    a = ""
    for s in matrix:
        print(f"{len(s)}")
        for p in s:
            a += f"{p:d}"
    print("{}".format(a))
