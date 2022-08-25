#!/usr/bin/python3
import dis
import marshal as ms

if __name__ == '__main__':
    with open('hidden_4.pyc', 'rb') as rof:
        rof.seek(16)
        dis.dis(ms.load(rof))
