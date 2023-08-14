#!/usr/bin/python3

"""
    a function that adds a new attribute to an object if it’s possible:
"""


def add_attribute(obj_ect, attribute, value):
    """
        adds a new attribute to an object
        we shall use paarameter object, atrribute and value
    """

    if not hasattr(obj_ect, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj_ect, attribute, value)
