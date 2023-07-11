#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
suffix = abs(number) % 10
if suffix > 5:
    suffix = suffix * -1
    print(f"Last digit of {number:d} is {suffix:d} and is greater than 5")
elif suffix == 0:
    print(f"Last digit of {number:d} is {suffix:d} and is 0")
elif suffix < 0 and not 0:
    print(f"Last digit of {number:d} is {suffix:d} and is less than 6 and not 0")
