#!/usr/bin/python3
"""
Defines the matrix_mul
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrix"""
    if type(m_a) != list:
        raise TypeError("m_a must be a list")
    b1 = len(m_a)
    if b1 == 0:
        raise ValueError("m_a can't be empty")
    b2 = None
    for i in m_a:
        if type(i) != list:
            raise TypeError("m_a must be a list of lists")
        if b2 is None:
            b2 = len(i)
            if b2 == 0:
                raise ValueError("m_a can't be empty")
        if b2 != len(i):
            raise TypeError("each row of m_a must should be of the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) != list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    b3 = None
    for i in m_b:
        if type(i) != list:
            raise TypeError("m_b must be a list of lists")
        if b3 is None:
            b3 = len(i)
            if b3 == 0:
                raise ValueError("m_b can't be empty")
        if b3 != len(i):
            raise TypeError("each row of m_b must should be of the same size")
        for j in i:
            if type(j) != int and type(j) != float:
                raise TypeError("m_b should contain only integers or floats")
    if b2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    matrix = []
    for i in range(b1):
        b = []
        for j in range(b3):
            n = 0
            for k in range(b2):
                n += m_a[i][k] * m_b[k][j]
            b.append(n)
        matrix.append(b)
    return (matrix)
