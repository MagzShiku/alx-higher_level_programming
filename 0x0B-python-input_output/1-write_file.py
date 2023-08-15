#!/usr/bin/python3

"""
    this function writes a string to a text file
    RETURNS: the number of characters written
"""


def write_file(filename="", text=""):
    """use with to make sure the file is automatically closed after"""
    with open(filename, mode='w', encoding='utf-8') as f:
        # w is for ipeninig a file
        return f.write(text)
