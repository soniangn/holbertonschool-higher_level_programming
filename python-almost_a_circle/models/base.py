#!/usr/bin/python3
"""module for Base class"""

class Base:
    """manage id attribute in all the classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
