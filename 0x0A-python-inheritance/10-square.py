#!/usr/bin/python3

"""
    defines a class Square that inherits frm rectang
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """define the class"""
    def __init__(self, size):
        """initialize the size with own property"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """return string that reps the rectangle"""
        return '[Square] {}/{}'.format(self.__size, self.__size)
