#!/usr/bin/python3

"""
    returns a dictionary description with simple data structures
    list, integer, dictionary, string, boolean
    obj is an instance of a class
"""


def class_to_json(obj):
    """returns dictionary with what I have named  above"""
    if not isinstance(obj, object):
        # obj is the instance of a class to be converted into JSON
        return obj

    json_obj = {}
    # initialized to store the converted data

    # iterate through the key_value pairs of the obj to get the data types
    # if it has the data structure, it is added to json_obj directory
    for key_pair, value_pair in obj.__dict__.items():
        if isinstance(value_pair, (list, dict, str, int, bool)):
            json_obj[key_pair] = value_pair
        elif isinstance(value_pair, object):
            json_obj[kay_pair] = class_to_json(value_pair)
    return json_obj
    # returns the variable json_obj which will contain converted data
