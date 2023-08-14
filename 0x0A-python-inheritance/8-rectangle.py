#!/usr/bin/python3

"""
    Write a class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """define the class"""
    def __init__(self, width, height):
        """initialize the pobjec with width and height"""
        self.__width = self.integer_validator('width', width)
        self.__height = self.integer_validator('height', height)

    def __str__(self):
        """return string reping the rectangle"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
