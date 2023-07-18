#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        n = add(a, b)
        n += sum([add(n, i) for i in range(4, 6)])
        return n
    else:
        return sub(a, b)
