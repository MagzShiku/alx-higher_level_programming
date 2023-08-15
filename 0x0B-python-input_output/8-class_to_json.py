#!/usr/bin/python3

"""
    returns a dictionary description with simple data structures
    list, integer, dictionary, string, boolean
    obj is an instance of a class
"""


def class_to_json(obj):
    """returns dictionary with what I have named  above"""
    if hasattr(obj, '__dict__'):
        """checking if it has an attribute of __dict__"""
        checked_obj = obj.__dict__.copy()
        # makes a copy of the obj with the attributes

        # iterate through the key/value pairs
        for main_key, main_value in checked_obj.items():
            if type(main_value) not \
                    in (int, float, bool, str, list, dict, type(None)):
                checked_obj = str(main_value)
        return main_value
    else:
        return {}
