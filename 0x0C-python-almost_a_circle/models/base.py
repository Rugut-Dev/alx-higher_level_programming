#!/usr/bin/python3
"""The Base of all classes for the project"""


class Base:
    """Manages id attribute in all future classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        self.id = __nb_objects += 1
