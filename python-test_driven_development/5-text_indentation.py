#!/usr/bin/python3
"""module that contains the function text_indentation(text)"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :"""
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    
    for character in text:
        print("{}".format(str(character)), end="")
        if character in ['.', '?', ':']:
            print("\n" * 2, end="")
