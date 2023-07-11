#!/usr/bin/python3
def islower(c):
    my_ascii = ord(c)
    if my_ascii >= 97 and my_ascii <= 122:
        return True
    else:
        return False
