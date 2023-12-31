#!/usr/bin/python3
"""
    Write a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:
    """define the class BaseGeometry"""
    def area(self):
        """raises Exception of area not implemented"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates the integer"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
