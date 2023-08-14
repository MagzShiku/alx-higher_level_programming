#!/usr/bin/python3
"""
    a function that returns the list of available attributes
    and methods of an object:
    without importing any module
"""


def lookup(obj):
    """
        this function  returns the list of available attributes
        and methods of an object
    """
    return dir(obj)
