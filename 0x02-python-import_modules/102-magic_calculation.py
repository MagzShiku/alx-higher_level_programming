#!/usr/bin/python3
from magic_calculation_102 import add, sub

def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        c += sum([add(c, i) for i in range(4, 6)])
        return c
    else:
        return sub(a, b)
