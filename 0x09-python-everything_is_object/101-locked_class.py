#!/usr/bin/python3

"""
    this function has no class or object attribute
    it prevents the user from dynamically creating a new instance
    attribute. Except if the new instance attribure is called first_name

    in this function, we do not import any module
"""


class LockedClass:
    """ We define the class LockedClass here"""
    __slots__ = "first_name"
    """
       we introduce __slots__ to a special attribute that
       can be defined in a class to specify a fixed set
       of attributes for instances of that class
    """
    def __init__(self):
        pass

    def __setattr__(self, attri_bute, value):
        if attri_bute == "first_name":
            super().__setattr__(attri_bute, value)
            """
                super(),  built in function that returns a temporary
                object of the superclass. It allows you to call methods
            """
        else:
            raise AttributeError("'LockedClass' object has no \
                    attribute '{}'".format(attri_bute))
