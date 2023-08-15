#!/usr/bin/python3
"""
    this writes an object to a text file
    using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """
        with makes sure a file is closed
        w is used for writing
    """
    with open(filename, 'w') as my_file:
        json.dump(my_obj, my_file)
