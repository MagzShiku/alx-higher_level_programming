#!/usr/bin/python3
"""
    adds all arguments to a Python list
    and saves them in a file
"""


import sys
# for error and exit
from os import path
# os if an operating system in python get the path
from typing import List
# The typing module provides support for type hints
# which are annotations that indicate the expected types
# of values in your code


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
# imports the function save_to_json_file from 5-save_to_json_file.py
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
# imports the function load_from_json_file from 6-load_from_json_file


def funct_adds_to_list(my_file: str, args: List[str]):
    """
        file gives list, the args in the lista are added
        saves the updated list to the file

        my_file: source file
        args: the args to be added
    """
    if not path.exists(my_file):
        save_to_json_file([], my_file)

    new_list = load_from_json_file(my_file)
    new_list.extend(args)

    save_to_json_file(new_list, my_file)


if __name__ == '__main__':
    my_file = 'add_item.json'
    args = sys.argv[1:]
    funct_adds_to_list(my_file, args)
