#!/usr/bin/python3


"""
    bring in the class Square
    this new class has a private instance __size
    and define the constructore __init__ to initialize
"""


class Square:
    """We initialize the square"""

    def __init__(self, size=0):
        """ int is the new square"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
