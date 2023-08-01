#!/usr/bin/python3

"""
    define the slass Square
"""


class Square:
    """ the Class has a private INstance __size. Then define a
        constructor method __init__
    """

    def __init__(self, size=0):
        """
            check if the inout size is an integer and
            is greater than or equal to 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """
        we define a new public instance areathat takes self
        as its only parameter
    """
    def area(self):
        return self.__size ** 2
