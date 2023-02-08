#!/usr/bin/python3
"""module for to_json_string method"""


import json

def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    json_str = json.dumps(my_obj)
    return json_str
