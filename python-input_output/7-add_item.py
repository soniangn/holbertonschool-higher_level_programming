#!/usr/bin/python3
"""module that adds all arguments to a Python list, and then saved to a file"""


import json
import sys
import os.path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

check_file = os.path.isfile(filename)

if check_file:
    pass
else:
    save_to_json_file([], filename)

new_file = load_from_json_file(filename)

for arg in sys.argv[1:]:
    new_file.append(arg)

save_to_json_file(new_file, filename)
