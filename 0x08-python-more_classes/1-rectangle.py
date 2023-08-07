#!/usr/bin/python3

"""
    rectangle class manipulates rectangles
    You can calculate areas
    you can divide areas etc

    FIRST, WE CALL THE CLASS, RECTANGLE
"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """
            __init__ initializes the width and height using the
            provided argiments, default to 0, if not specified
        """
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return self.__height
        """
            this defines the height, just like the width does
            returns value of provate width
        """

    @height.setter
    def height(self, value):
        """
            sets the height of the rectangle, and shoes errors if the
            height is < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width
    """
        def width(self) defines width: this method gets the
        width attribute
        when you return self.__width, you will return the value
        of the private width
    """

    @width.setter
    def width(self, value):
        """
            sets the width of the rectangle
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
