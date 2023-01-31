#!/usr/bin/python3
"""module that contains the function text_indentation(text)"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :"""
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    after_new_line = False
    for c in text:
        if after_new_line:
            if c == " ":
                continue
            after_new_line = False
        if c in ['.', '?', ':']:
            print(c)
            print("")
            after_new_line = True
        else:
            print(c, end="")
