#!/usr/bin/python3

"""
    this creates a JSON from an object file
    we use load
    we use with
"""

import json


def load_from_json_file(filename):
    """load loads the object, r for read"""
    with open(filename, 'r') as my_file:
        return json.load(my_file)
