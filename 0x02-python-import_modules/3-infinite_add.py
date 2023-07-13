#!/usr/bin/python3
import sys

from decimal import Decimal

if __name__ == "__main__":
    the_arg = sys.argv[1:]
    all_args = Decimal(0)
    for arg in the_arg:
        all_args += Decimal(arg)
    print(str(all_args))
