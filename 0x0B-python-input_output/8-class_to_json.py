#!/usr/bin/python3

"""
    returns a dictionary description with simple data structures
    list, integer, dictionary, string, boolean
    obj is an instance of a class
"""


def class_to_json(obj):
    """returns dictionary with what I have named  above"""
    if not isinstance(obj, object):
        return obj

    json_obj = {}

    for key_pair, value_pair in obj.__dict__.items():
        if isinstance(value_pair, (list, dict, str, int, bool)):
            json_obj[key_pair] = value_pair
        elif isinstance(value_pair, object):
            json_obj[kay_pair] = class_to_json(value_pair)
    return json_obj
