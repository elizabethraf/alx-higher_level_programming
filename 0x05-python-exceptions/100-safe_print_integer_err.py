#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
    except Exception as item:
        print("Exception:", item, file=sys.stderr)
        return False
    else:
        return True
