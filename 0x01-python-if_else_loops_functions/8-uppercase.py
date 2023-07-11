#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        my_ascii = ord(c)
        if my_ascii >= 97 and my_ascii <= 122:
            res += chr(my_ascii - 32)
        else:
            res += c
    print(res)


