#!/usr/bin/python3
"""
    a class Rectangle that inherits from BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """define the class"""
    def __init__(self, width, height):
        """initialize the own property(self) for h & W"""
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """get the area"""
        return self.__width * self.__height

    def __str__(self):
        """get a string to rep the rectangle"""
        return '[Rectangle] {}/{}'.format(self.__width, self.__height)
