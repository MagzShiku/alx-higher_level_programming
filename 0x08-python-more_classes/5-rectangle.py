#!/usr/bin/python3
"""
    Write a class Rectangle that defines a rectangle by:
    (based on 4-rectangle.py)
"""


class Rectangle:
    """
        Write a class Rectangle that defines a rectangle by:
        (based on 4-rectangle.py)
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            this sets the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            after getting the value from the above function
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            obtain the value of height from public
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            sets the values of height while
            checking for the min and intness of it
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            sets the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            prints the representative og the rectangle using # symbol
            returns the rectngle
        """
        if self.__width == 0:
            return ""
        if self.__height == 0:
            return ""

        my_shape = ""
        for char in range(self.__height):
            for char_2 in range(self_width):
                my_shape += "#"

            if char != self.__height - 1:
                my_shape += "\n"
        return my_shape

    def __repr__(self):
        """
            takes object and represents it as a string
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
            deletes the rectangle
        """
        print("Bye rectangle...")
