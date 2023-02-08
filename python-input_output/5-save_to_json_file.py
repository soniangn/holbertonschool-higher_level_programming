#!/usr/bin/python3
"""module for save_to_json_file method"""


import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as f:
        json_obj = json.dumps(my_obj)
        wr_object = f.write(json_obj)
        return wr_object 
