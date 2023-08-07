#!/usr/bin/python3
"""
    this function:
    Write a class Rectangle that defines a rectangle by:
    (based on 6-rectangle.py)
"""


class Rectangle:
    """
        calling the class Rectangle
        to allow us to perform fun things with rectangles
    """
    number_of_instances = 0

    print_symbol = "#"
    """we initialize the symbol """

    """
        number of instances checls how many times the rectangle
        has been created.
        we have initialised the number_of_instances
        starting from 0.
        We need the instances to be looped into at first,
        then decrementwed towards the end.
    """
    def __init__(self, width=0, height=0):
        """
            initialise the function
            using the parameters height, width againt the self
        """
        self.width = width
        self.height = height

        type(self).number_of_instances += 1

    @property
    def width(self):
        """this gets the width from public"""
        return self.__width

    @width.setter
    def width(self, value):
        """
            sets the value of the width
            chacks that the value is an int
            and if the value of width is >= 0
            then prints the respective errors
        """
        if type(value) is not int:
            return TypeError("width must be an integer")
        if value < 0:
            return ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ gets the value of the height from public"""
        return self.__height

    @height.setter
    def height(self, value):
        """
            sets the value of the height
            chacks that the value is an int
            and if the value of height is >= 0
            then prints the respective errors
        """
        if type(value) is not int:
            return TypeError("height must be an integer")
        if value < 0:
            return ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ gets area of rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """gets perimeter of the rectangle"""
        if self.__height == 0:
            return 0
        if self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
            represents the rectangle as a string
            returns empty string as ""
            and also gives a new line after the representation
        """
        if self.__height == 0:
            return ""
        # checks if the rectangle is not there then returns empty string

        if self.__width == 0:
            return ""
        # same for the width
        """creates a variable my_shape and initialies it with empty"""

        my_shape = ""
        for char in range(self.__height):
            my_shape += str(self.print_symbol) * self.__width

            if char != self.__height - 1:
                my_shape += "\n"
        return my_shape

    def __repr__(self):
        """prints the string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
            deletes the rectangle created
            decrements while deleting the other created rectangles
        """
        type(self).number_of_instances -= 1

        # prints the ending of the function
        print("Bye rectangle...")
