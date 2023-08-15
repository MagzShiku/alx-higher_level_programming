#!/usr/bin/python3

"""
    write a class student
    that defines a student by: first_name, last_name, age
"""


class Student:
    """defines the student by the below parameters"""
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        """lets give then their own properties"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
    # the dict ch3cks for attributes in the object
