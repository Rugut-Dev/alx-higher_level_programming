#!/usr/bin/python3
"""Returns the __dict__ that are serializable"""


def class_to_json(obj):
    """returns dict"""
    ser_attributes = {}
    for attr, val in obj.__dict__.items():
        if isinstance(val, (list, dict, str, int, bool)):
            ser_attributes[attr] = val
    return ser_attributes
