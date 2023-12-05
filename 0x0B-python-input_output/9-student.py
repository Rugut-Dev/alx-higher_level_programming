#!/usr/bin/python3
"""class Student that defines student"""


class Student:
    """Class Student that retrieves its dict rep"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        ser_attributes = {}
        for attr, val in self.__dict__.items():
            if isinstance(val, (str, int)):
                ser_attributes[attr] = val
        return ser_attributes
