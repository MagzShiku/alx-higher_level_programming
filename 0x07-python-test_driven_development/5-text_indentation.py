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

    text = text.strip()
    punctuations = [".", "?", ":"]

    for p in punctuations:
        text = text.replace(p, p + "\n")
    lines = [line.strip() for line in text.split("\n")]
    for i, line in enumerate(lines):
        print(line)
        if line and i < len(lines) - 1:
            print()
