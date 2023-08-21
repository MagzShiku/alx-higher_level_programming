#!/usr/bin/puthon3

"""
this class inherits from Base
there are several private instance attr I have been asked to work with
width, height, x and y
i have been given the constructor method as well
"""


"""
we shall initialise 2 variables with __import__
"""

"""
module_name = 'module.base'
class_name = 'Base'

module = __import__(module_name, fromlist=[class_name])
Base = getattr(module, class_name)
"""

from models.base import Base


class Rectangle(Base):
    """this helps us make a triangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        """we give private attributes to the parameters"""

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
