#!/usr/bin/python3
import random
signedNumber = random.randint(-10, 10)
if signedNumber > 0:
    print(f"{signedNumber:d} is positive")
elif signedNumber == 0:
    print(f"{signedNumber:d} is zero")
elif signedNumber < 0:
    print(f"{signedNumber:d} is negative")
