#!/usr/bin/python3
"""checks instance of a class"""


def inherits_from(obj, a_class):
    """checks if variable is subclass"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
