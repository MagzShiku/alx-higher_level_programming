#!/usr/bin/python3

"""
    in this module, we define a class MyInt that inherits frm int
"""


class MyInt(int):
    """define the class"""
    def __eq__(self, other):
        """
            the eq is equal operator
            the module Overrides the equality (==) operator.
            it will return the opposite of the default behavior
            True if objects are not eqial and False if they are equal
        """
        return int(self) != int(other)

    def __ne__(self, other):
        """not equal"""
        return int(self) == int(other)
