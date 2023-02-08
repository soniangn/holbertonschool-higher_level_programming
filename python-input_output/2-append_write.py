#!/usr/bin/python3
"""module for append_write method"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        write_file = f.write(text)
        return write_file
