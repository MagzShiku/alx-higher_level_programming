#!/usr/bin/python3

"""
write a class Student
defines student based in first_name, last_name, age
"""


class Student:
    """defines a new class Student"""
    first_name = ""
    last_name = ""
    age = ""
    # initialized them with empty strings for now

    def __init__(self, first_name, last_name, age):
        """initilization method using the parameters"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        # self gives own propoerty to the parameters

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__

        json_obj = {}

        for attr_dict in attrs:
            if hasattr(self, attr_dict):
                json_obj[attr_dict] = getattr(self, attr_dict)
        return json_obj
