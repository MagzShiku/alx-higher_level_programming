#!/usr/bin/python3
"""
    this module reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
        the parameter here if the filename... ie File
    """
    with open(filename, encoding='utf-8') as f:
        """with helps you automatically close the file"""
        for ln in f:
            # eiterate through the entore file
            print(ln, end="")
            # here the end of the file will return an empty string
