#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        item = fct(*args)
    except Exception as item:
        print("Exception:", item, file=sys.stderr)
        return None
    return (item)
