#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        item = a / b
    except ZeroDivisionError:
        item = None
    finally:
        print("Inside result: {}".format(item))
    return (item)
