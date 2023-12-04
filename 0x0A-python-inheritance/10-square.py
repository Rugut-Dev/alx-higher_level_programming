#!/usr/bin/python3
"""Based on 6-base_geometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        """returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """Informal string rep"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
