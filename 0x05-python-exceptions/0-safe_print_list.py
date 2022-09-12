#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    try:
        for list in my_list:
            if y < x:
                print("{:d}".format(list), end="")
                y += 1
    except TypingError as x:
        print()

    print()
    return (y)
