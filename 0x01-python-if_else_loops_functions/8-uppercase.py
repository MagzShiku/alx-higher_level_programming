#!/usr/bin/python3
def xUpper(i):
    my_C = ord(i)
    if my_C >= 97 and my_C <= 122:
        return (my_C - 32)
    else:
        return (my_C)



def uppercase(str):
    res = ""
    for i in str:
        res += "%c" % xUpper(i)
    print("{:s}".format(res))
