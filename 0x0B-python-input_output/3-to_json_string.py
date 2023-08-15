#!/usr/bin/python3
"""
    this function returns JASON
    Java Script Object Notation
    a data interchange format used for transmitting data
    between Server and Web App
"""


import json


def to_json_string(my_obj):
    """represent an object as a string"""
    return json.dumps(my_obj)
