#!/usr/bin/python3
"""Based on 6-base_geometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from square"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", self.__size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
