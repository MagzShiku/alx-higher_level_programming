#!/usr/bin/python3

"""
    Write a class Rectangle that defines a rectangle by:
    (based on 7-rectangle.py)
    then adds several more features
    this should be fun
"""


class Rectangle:
    """we shall define the symbol printer and instance counter"""

    number_of_instances = 0
    # inittialized to 0

    print_symbol = "#"
    # initialized to #

    def __init__(self, width=0, height=0):
        """
            This is a constructor method
            itll use self with the parameters width and height
        """
        self.width = width
        self.height = height

        type(self).number_of_instances += 1
        # we shall increment/loop to check all rectangles created

    @property
    def width(self):
        """begetter of the width method"""
        return self.__width

    @width.setter
    def width(self, value):
        """
            this method sets the value of the width
            it checks if the value is int
            and if the value is >= 0
            then assigns value to the width
        """
        if type(value) is not int:
            return TypeError("width must be an integer")
        if value < 0:
            return ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method that gets the width"""
        return self.__height

    @height.setter
    def height(self, value):
        """
            this method sets the value of the height
            it checks if the value is int
            and if the value is >= 0
            then assigns value to the height
        """
        if type(value) is not int:
            return TypeError("height must be an integer")
        if value < 0:
            return ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """this gets the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """this gets the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
            this is a string representation of a rectangle
            returns a represrntation
            if the rectangle is empty/not there, return empty string""
        """
        if self.width == 0 or self.height == 0:
            return ""

        else:
            my_shape = ((str(self.print_symbol) * self.width) + '\n') \
                    * self.height
            return my_shape[:-1]
        # return the last digit of the string

    def __repr__(self):
        """
            checks the string representation of an object
            returns the string representation of the object
            as a formated string
        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    @classmethod
    def __del__(self):
        """
            this deletes the rectangle
            it then decrements looking for other rectangles created
            by instances, then deletes them too
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            this static method looks at the size of the rectangles
            returns the larger rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        else:
            return rect_2
