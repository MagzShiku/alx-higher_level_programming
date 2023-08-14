#!/usr/bin/python3
"""
    a class MyList that inherits list
    Public instance method: def print_sorted(self):
    that prints the list, but sorted (ascending sort)
    You can assume that all the elements of the list will be of type int
"""


class MyList(list):
    """inherit list class and add to new method print"""
    def print_sorted(self):
        """print the sorted list in ascending order"""
        print(sorted(self))
