#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 3-square.py)"""


class Square:
    """class Square defining a square, privately instantiating size"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """getter property for getting return from setter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter function for value passed with error checking"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns area of a square given size"""
        return self.__size * self.__size
