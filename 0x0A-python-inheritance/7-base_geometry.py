#!/usr/bin/python3
"""Based on 6-base_geometry"""


class BaseGeometry:
    """Raises an exeception that area() is not implemented
validates value

"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
