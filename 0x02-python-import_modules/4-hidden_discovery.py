#!/usr/bin/python3
import dis, types
import marshal as ms

def stored_code(mycode, spaces=''):
    for const in mycode.co_consts:
        if type(const) != types.CodeType and const is not None:
            if not const.startswith("_"):
                print(f"{const}")

if __name__ == '__main__':
    with open('hidden_4.pyc', 'rb') as rof:
        rof.seek(16)
        store = ms.load(rof)
    stored_code(store)


