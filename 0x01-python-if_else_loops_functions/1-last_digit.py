#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
suffix = abs(number) % 10
if number < 0:
    suffix = -suffix
    print(f"Last digit of {number:d} is {suffix:d} and is ",  end="")
if suffix > 5:
    print("greater than 5")
elif suffix == 0:
    print("0")
else:
    print("less than 6 and not 0")
