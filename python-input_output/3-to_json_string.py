#!/usr/bin/python3
import json
"""module for to_json_string method"""


def to_json_string(my_obj):
    json_str = json.dumps(my_obj)
    print(json_str)
