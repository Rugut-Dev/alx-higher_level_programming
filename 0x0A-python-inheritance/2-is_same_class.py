#!/usr/bin/python3
"""returns True if object is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    """function checking isinstance"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
