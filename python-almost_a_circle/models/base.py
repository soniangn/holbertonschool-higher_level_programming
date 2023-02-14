#!/usr/bin/python3
""" module for Base class """
import json
import os.path


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
            return []
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        filename = "{}.json".format(cls.__name__)

        json_dict = []

        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None or list_objs == []:
                f.write("[]")
            else:
                for obj in list_objs:
                    dictionary = cls.to_dictionary(obj)
                    json_dict.append(dictionary)
                    dict_to_string = cls.to_json_string(json_dict)
                f.write(dict_to_string)

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

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        new_list = []
        check_file = os.path.isfile(filename)
        if not check_file:
            return []
        else:
            with open(filename, "r", encoding="utf-8") as f:
                read_data = f.read()
                json_list = cls.from_json_string(read_data)
                for dict in json_list:
                    new_list.append(cls.create(**dict))
                return new_list
