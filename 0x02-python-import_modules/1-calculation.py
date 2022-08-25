#!/usr/bin/python3
from calculator_1 import add, mul, div, sub
if __name__ == '__main__':
    a = 10
    b = 5
    result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))
    result = sub(a, b)
    print("{:d} - {:d} = {:d}".format(a, b, result))
    result = mul(a, b)
    print("{:d} * {:d} = {:d}".format(a, b, result))
    result = div(a, b)
    print("{:d} / {:d} = {:d}".format(a, b, result))
