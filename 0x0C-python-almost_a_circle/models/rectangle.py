#!/usr/bin/python3

"""
this class inherits from Base
there are several private instance attr I have been asked to work with
width, height, x and y
i have been given the constructor method as well
"""


from models.base import Base
"""
inherit from base file
"""


class Rectangle(Base):
    """
    this helps us make a rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        this initiates the parameters with self
        """
        super().__init__(id)
        """
        the super calls the method from the parent class
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.id = id
        """
        we give private attributes to the parameters
        """

    @property
    def width(self):
        """
        this gives the width a property
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        this method sets the lavlue to the width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        sets the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        This gives the value of the height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        sets the propoerty of the x parameter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        sets the value to the x parameter
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        defines the parameter y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        sets value to the parameter y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        this is the formulat to get the area of the rectangle
        """
        return self.width * self.height

    def display(self):
        """
        this displays the rectangle as a # element
        """
        for n in range(self.y):
            print()
        for n in range(self.height):
            print(" " * self.x + "#" * self.width)

    def update(self, *args):
        """
        this module updats the values
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]

    def __str__(self):
        """
        this method reprsents the rectangle as a string
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
