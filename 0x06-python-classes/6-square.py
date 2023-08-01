#!/usr/bin/python3
"""
    define Class Square with provate instance attibute __size & __position
"""


class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
            assign input size and position to the private
            attributes __size and __position directly.
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
            greates a getter method
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            cretaes setter method
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    """
        creates setter method
    """
    def position(self, value):
        if not isinstance(value, tuple) or len(value)
        != 2 or not isinstance(value[0], int) or
        not isinstance(value[1], int) or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()

        else:
            for num in range(self.__position[1]):
                print()
            for num in range(self.__size):
                print(" " * self.__position[0], end="")
                for val in range(self.__size):
                    print("#", end="")
                print()
