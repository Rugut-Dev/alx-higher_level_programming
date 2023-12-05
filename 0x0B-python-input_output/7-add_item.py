#!/usr/bin/python3
"""script that adds all args to a python list and tehn save them to a file"""

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import json
import sys

try:
    with open('add_item.json', 'x') as file:
        file.write('[]')
except FileExistsError:
    pass

cmd_args = sys.argv[1:]
data = load_from_json_file('add_item.json')
if data is None:
    data = []

data.extend(cmd_args)

save_to_json_file(data, 'add_item.json')
