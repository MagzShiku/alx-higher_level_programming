#!/usr/bin/python3
"""
creates a class Student
defined by first_name, last_name & age
"""


class Student:
    """class defined, now lets initiate with empty"""
    first_name = ""
    last_name = ""
    age = ""

    def __init__(self, first_name, last_name, age):
        """lets give self property to the parameters (key-value pairs)"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__

        json_obj = {}

        for attr_dict in attrs:
            if hasattr(self, attr_dict):
                json_obj[attr_dict] = getattr(self, attr_dict)
        return json_obj

    def reload_from_json(self, json):
        """
            replaces all attributes of the Student instance
            assume json will always be a dictionary
            A dictionary key will be the public attribute name
            A dictionary value will be the value of the public attribute
        """
        for key_pair, value_pair in json.items():
            setattr(self, key_pair, value_pair)
