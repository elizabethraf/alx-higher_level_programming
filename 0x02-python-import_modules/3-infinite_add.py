#!/usr/bin/python3
from sys import argv
if __name__ == '__main__':
    i = len(argv)
    if i < 2:
        print("0")
    else:
        if i == 2:
            sum = 0 + int(argv[i-1])
            print(f"{sum:d}")
        elif i > 2:
            sum = 0
            for k in range(1, i):
                sum +=int(argv[k])
            print(f"{sum:d}")
