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
