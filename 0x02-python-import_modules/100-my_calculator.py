#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


OPERATIONS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, the_operator, b = sys.argv[1:]

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Error: arguments must be integers")
        sys.exit(1)

    try:
        func = OPERATIONS[the_operator]
    except KeyError:
        print("Unknown operator. Available operations: +, -, * and /")
        sys.exit(1)
    out_put = func(a, b)
    print("{} {} {} = {}". format(a, the_operator, b, out_put))
