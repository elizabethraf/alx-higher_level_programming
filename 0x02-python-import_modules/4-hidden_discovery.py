#!/usr/bin/python3
import dis
import types
import marshal as ms


def stored_code(mycode):
    for const in mycode.co_consts:
        if not isinstance(const, types.CodeType) and const is not None:
            if not const.startswith("_"):
                print(f"{const}")


if __name__ == '__main__':
    with open('hidden_4.pyc', 'rb') as rof:
        rof.seek(16)
        store = ms.load(rof)
    stored_code(store)
