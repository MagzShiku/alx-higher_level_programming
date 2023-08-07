#!/usr/bin/python3
"""
    Write a class Rectangle that defines a rectangle by:
    (based on 3-rectangle.py)
"""


class Rectangle:
    """
        clall the rectangle class
        Rectangle allows you to manipulate rectangles
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            allows you to get the width from
            public
            returns the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            this is the width getter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            allows you to get height from public
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            this lets you define the height of the rectangle
            then it checks for parameters on if it is int and less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            this gets the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            gets the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
             returns a string representation of the rectangle
             with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ((("#" * self.__width) + "\n")
                * (self.__height - 1)) + ("#" * self.__width)

    def __repr__(self):
        """
            method returns a string representation of the object in a
            format that can be used with the eval function to recreate
            the object
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)
