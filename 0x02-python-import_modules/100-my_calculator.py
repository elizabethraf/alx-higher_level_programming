#!/usr/bin/python3
from calculator_1 import add, mul, div, sub
from sys import argv
if __name__ == '__main__':
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
    a = (argv[1])
    b = (argv[3])
    opr = sys.argv[2]

    result = add(a, b)
    if argv[2] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, result))
    result = sub(a, b)
    if argv[2] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, result))
    result = mul(a, b)
    if argv[2] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, result))
    result = div(a, b)
    if argv[2] == "/":
        print("{:d} / {:d} = {:d}".format(a, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
