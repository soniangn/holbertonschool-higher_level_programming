#!/usr/bin/python3
"""module for Base class"""
import json


class Base:
    """manage id attribute in all the classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initializes the id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
