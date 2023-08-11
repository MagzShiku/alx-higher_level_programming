#!/usr/bin/puthon3

"""
    Write a function that prints a text with 2 new lines
    after each of these characters: ., ? and :
"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in [".", "?", ":"]:
        text = text.replace(char, char + "\n\n")
        rows = [line.strip() for line in text.split("\n")]

        for line in rows:
            print(line)

            if line:
                print()
