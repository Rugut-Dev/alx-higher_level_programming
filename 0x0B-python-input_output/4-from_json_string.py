#!/usr/bin/python3
"""func that returns an object rep by JSON"""
import json


def from_json_string(my_str):
    """uses json.loads to return python object"""
    return json.loads(my_str)
