#!/usr/bin/python3
"""
    a function that returns True if the object is an instance of
    a class that inherited (directly or indirectly) frm
    the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """
        a function that returns True if the object is an instance of
        a class that inherited (directly or indirectly) frm
        the specified class ; otherwise False.
    """

    return isinstance(obj, type) and issubclass(obj,
            a_class) and type(obj) != a_class
