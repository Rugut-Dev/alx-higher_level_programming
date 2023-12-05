#!/usr/bin/python3
"""func that returns the JSON rep of an object"""
import json


def to_json_string(my_obj):
    """returns JSON from python object"""
    return json.dumps(my_obj)
