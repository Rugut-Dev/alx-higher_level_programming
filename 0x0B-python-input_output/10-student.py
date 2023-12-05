#!/usr/bin/python3
"""class Student that defines student"""


class Student:
    """Class Student that retrieves its dict rep"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        ser_attributes = {}
        for attr in attrs:
            if hasattr(self, attr):
                ser_attributes[attr] = getattr(self, attr)
        return ser_attributes
