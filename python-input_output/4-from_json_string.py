#!/usr/bin/python3
"""module for from_json_string method"""


import json


def from_json_string(my_str):
    """returns an object (Python data structure)""" 
    """represented by a JSON string"""
    json_str = json.loads(my_str)
    return json_str
