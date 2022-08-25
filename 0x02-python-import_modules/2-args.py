#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    i = len(argv)
    if i < 2:
        print("0 arguments.")
    else:
        if i == 2:
            print("1 argument:")
            print("{:d}: {:s}".format(i-1, argv[i-1]))
        elif i > 2:
            print(f"{i-1:d} arguments:")
            for k in range(1, i):
                print("{:d}: {:s}".format(k, argv[k]))
