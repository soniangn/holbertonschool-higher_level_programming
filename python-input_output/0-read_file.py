#!/usr/bin/python3
"""module for read_file method"""


def read_file(filename=""):
    """reads a text file"""
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
