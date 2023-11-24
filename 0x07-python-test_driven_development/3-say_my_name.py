#!/usr/bin/python3
"""Holds say_my_name function

Prints a string with placeholders for first_name and last_name.
Performs checks on the passed args and raises Exceptions as expected
"""


def say_my_name(first_name, last_name=""):
    """ Checks the passed args(first_name and last_name) for TypeErrors"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
