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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        this saves the csv file with json
        """
        my_file = cls.__name__ + ".json"
        content = []
        if list_objs is not None:
            content = [obj.to_dictionary() for obj in list_objs]
        with open(my_file, "w") as fl:
            fl.write(cls.to_json_string(content))

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create a dummy instance with mandatory attributes
        Call update method to apply real values
        """
        new_instance = cls(1, 1)
        new_instance.update(**dictionary)
        return new_instance
        # new_instance is the dummy instance created
