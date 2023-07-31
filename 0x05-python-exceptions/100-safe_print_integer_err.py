#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    if not isinstance(value, int):
        sys.stderr.write("Exception: input value must be an integer\n")
        return False
    try:
        sys.stdout.write("{:d}\n".format(value))
        return True
    except ValueError as ve:
        sys.stderr.write("Exception: {}\n".format(ve))
        return False
