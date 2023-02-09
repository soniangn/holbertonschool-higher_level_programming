#!/usr/bin/python3
"""module that adds all arguments to a Python list, and then saved to a file"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    arg_list = []

    obj_list = load_from_json_file('add_item.json')

    for arg in sys.argv[1:]:
        arg_list.append(arg)

    save_to_json_file(arg_list, 'add_item.json')

except: 
    for arg in sys.argv[1:]:
            arg_list.append(arg)

    save_to_json_file(arg_list, 'add_item.json')
