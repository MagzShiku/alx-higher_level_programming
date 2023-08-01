#!/usr/bin/python3

"""a class Square that defines a square by: (based on 0-square.py)"""
"""Why size is private attribute?"""


class Square:
    """init is a constructor method that uses the attribute size"""
    def __init__(personal, size):
        """the size cannot be modified from outside the class"""
        personal.__size = size
