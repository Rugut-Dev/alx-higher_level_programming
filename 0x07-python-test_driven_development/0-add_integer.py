#!/usr/bin/python3
"""Addition of integers

This module provides a function to add two integers or floats.
It checks the types of input parameters and returns their sum as an integer.
"""

def add_integer(a, b=98):
    """Returns an integer: addition of a and b"""
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
