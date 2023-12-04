#!/usr/bin/python3
"""Attempts to add a new attribute to an object"""


def add_attribute(obj, attr, value):
    """Adds a new attribute to an object if possible"""
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if (not hasattr(obj, attr)):
        obj.__setattr__(attr, value)
