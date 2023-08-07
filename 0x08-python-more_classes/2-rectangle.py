#!/usr/bin/python3
"""
    Write a class Rectangle that defines a rectangle by:
    (based on 1-rectangle.py)
"""


class Rectangle:
    """
        Instantiation with optional width and height:
        def __init__(self, width=0, height=0):
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            retrieves the width of the rectangle
            returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        sets the width of the rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        retrieves the height of the rectangle
        returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            accounts for type and value errors in case
            the values entered are not ints or are < 0
            then sets the self.__height to value
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            this returns the area of the rectangle
            by accessing the values set int the width and height
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            this function gets the perimeter of the h * 2 and w * 2
            i think I will write the function I want here
        """
        if self.__width == 0:
            return 0
        if self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
