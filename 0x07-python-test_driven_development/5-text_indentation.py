#!/usr/bin/puthon3

"""
    Write a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
        we define the function here, then the error message
        Write a function that prints a text with 2 new lines
        after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()
            i += 1
        else:
            print(text[i], end="")
            i += 1
