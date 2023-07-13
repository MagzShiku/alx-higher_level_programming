#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
a = 10
b = 5
print("{a} + {b} = {sum}".format(a=a, b=b, sum=add(a, b)))
print("{a} - {b} = {_sub}".format(a=a, b=b, _sub=sub(a, b)))
print("{a} * {b} = {mult}".format(a=a, b=b, mult=mul(a, b)))
print("{a} / {b} = {_div}".format(a=a, b=b, _div=div(a, b)))
