#!/usr/bin/python3

"""
    a function that inserts a line of text to a file,
    after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    with open(filename, mode='r+', encoding='utf-8') as my_file:

        row = my_file.readlines()
        my_file.seek(0)

        for ln in row:
            my_file.write(ln)

            if search_string in ln:
                my_file.write(new_string)
        my_file.truncate()
