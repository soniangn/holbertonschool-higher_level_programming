#!/usr/bin/python3
"""module for is_same_class method"""


def is_same_class(obj, a_class):
    """checks instance object"""
    return True if isinstance(obj, a_class) else False
