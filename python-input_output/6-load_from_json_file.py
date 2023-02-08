#!/usr/bin/python3
"""module for load_from_json_file method"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file"""
    with open(filename, encoding="utf-8") as f:
       json_file = f.read()
       obj = json.loads(json_file)
       return obj
 