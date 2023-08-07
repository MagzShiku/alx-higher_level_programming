#!/usr/bin/python3

"""
    Write a class Rectangle that defines a rectangle by:
    (based on 5-rectangle.py)
"""


class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """
            Write a class Rectangle that defines a rectangle by:
            this initializes the class
            using the parameters
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        """
            number_of_instances chacks the number of instances
            of the rectangle class that has been created
        """

    @property
    def width(self):
        """
            this function allows us to gather width value from public
            returns: self.__width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            this sets the value of the width
            while checking for int value
            the width should be int
            the value of value should be >= 0
        """
        if type(value) is not int:
            return TypeError("width must be an integer")
        if value < 0:
            return ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            this function allows us to gather height into from publuc
            returns the height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            this function sets value to the height
            while checking to see if the height is an int
            and also checking if the value is less than 0
            returns the value
        """
        if type(value) is not int:
            return TypeError("height must be an integer")
        if value < 0:
            return ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            gets area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            returns the perimeter of the rectangle
        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            this function represents the rectangle as a string using
            the symbol #
            then brings a ne line
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        my_shape = ""
        for char in range(self.__height):
            for char_2 in range(self.__width):
                my_shape += "#"

            if char != self.__height - 1:
                my_shape += "\n"
        return my_shape

    def __repr__(self):
        """
            this represents the object as string
            returns formated string
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
            this deletes the rectangle
            then decrements all the instances when the rectanle is created
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
        # this decrements the instances when the rectangle was created
