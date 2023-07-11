#!/usr/bin/python3
def uppercase(_upper):
    for c in _upper:
        my_ascii = ord(c)
        if my_ascii >= 97 and my_ascii <= 122:
            ascii_upper = my_ascii - 32
            print("{}".format(chr(ascii_upper)), end='')
        else:
            print("{}".format(c), end='')
    print()
