#!/usr/bin/python3
"""
    Write a class Rectangle that defines a rectangle by:
    (based on 2-rectangle.py)
"""


class Rectangle:
    """
        we start by definigng the class Rectangle
        then the function with the parameters self, width & height
    """
    def __init__(self, width=0, height=0):
        """
            Write a class Rectangle that defines a rectangle by:
            (based on 2-rectangle.py)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
            extract the width from pudlic
            return the width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            sets the value of the width
            it also raises the TypeError and Value Error
            depending on the value of value being more than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            extracts the value of height from public
            returns height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            this  function gets the height of the rectangle
            checks for ValueError and TypeError
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            this returns the area of the rectangle
            takes the width * height
        """
        return (self.__width * self.__height)

    def perimeter(self):
        """
            this function returns the perimeter of teh rectangle
            if width or height is equal to 0, perimeter has to be equal to 0
            print() and str() should print the rectangle
            with the character #: (see example below)
            if width or height is equal to 0, return an empty string
        """
        if self.__width == 0:
            return 0
        if self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def string_rep_obj(self):
        """
            this function should print the rectangle with the character #
            this is a self made function name for the task __rpr__
            we shall check if the width and height are == 0
            if they are, our function should return an empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ""
            # returns empty string
        my_string = ""
        for char in range(self.__height):
            my_string += "#"

            if char != self.__height - 1:
                my_string += "\n"
        return my_string

    def __str__(self):
        """
            the __str__ represents an object as a string
            allows for us to print an instance directly
            retunrs output of string_rep_obj function
        """
        return self.string_rep_obj()
