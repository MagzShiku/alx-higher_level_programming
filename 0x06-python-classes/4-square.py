#!/usr/bin/python3

""" define Square"""


class Square:
    """
        initialize with __init__ with uses self and
        size as parameters
    """
    def __init__(self, size=0):
        self.__size = size
        """
            @property is a decorator ofr the size attribure to create
            a getter method
        """
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    """
        define a new public instance method called area that
        takes self as iys only parameter
    """
    def area(self):
        return self.__size ** 2
