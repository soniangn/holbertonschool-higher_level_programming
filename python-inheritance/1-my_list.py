#!/usr/bin/python3
"""module for MyList class"""

class MyList(list):
    """prints a sorted list"""
    def __init__(self):
        """initialises instance"""
        pass

    def print_sorted(self):
        """method that prints a sorted list"""
        print(sorted(self))
