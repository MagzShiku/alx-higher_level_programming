#!/usr/bin/python3
"""
    define Square
"""


class Square:
    """
        define __init__: intiate it with self and size attributes
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """
            this decorator @property for the size attribute
            to create a getter method
            this allows us to retrieve the private __size from
            the outside of the class
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            this decorator to create a setter method
            which checks if the input size is an integer
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    """
        define a new public instance method: Area
        it returns the area of the Square
    """
    def area(self):
        return self.__size ** 2
    """
        define a new public instance method that
        prints out the Square of the character ##
    """
    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for i in range(self.__size):
                for num in range(self.__size):
                    print("#", end="")
                print()
