#!/usr/bin/python3
""" module for Base class """
import json


class Base:
    """
    represents base class for all others models

    __nb_objects: number of instantiated base

    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)

        print(list_objs)

        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_obj = cls.to_json_string(list_objs)
                f.write(json_obj)

    @staticmethod
    def from_json_string(json_string):
        """ returns list of json string representation """
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set """
        dummy = cls(5, 3)
        dummy.x = 0
        dummy.update(**dictionary)
        return dummy
