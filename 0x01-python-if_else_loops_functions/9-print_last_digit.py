#!/usr/bin/python3
def print_last_digit(number):
    num = int(str(abs(number))[-1])
    print(num, end='')
    return (num)
