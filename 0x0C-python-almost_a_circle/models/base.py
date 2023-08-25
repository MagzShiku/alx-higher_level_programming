#!/usr/bin/python3
"""
    this base class manages the id attribute in my future classes
    and to avoind duplicating the same code and some bugs by extension
"""

import json


class Base:
    """
    here we define the class. It worksa s the main file i think
    """
    __nb_objects = 0
    """
        this is a provateclass attribute method
        this keeps track of the number of objectc created from this class
    """
    def __init__(self, id=None):
        """we initialize method with init, and set id to None as default"""
        if id is not None:
            """
                assigns the value of id to a public instance attribute self.id
                otherwise, it increments it, iterating through the values
            """
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns a JSON string representation of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
