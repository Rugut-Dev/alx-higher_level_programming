#!/usr/bin/python3
"""class Rectangle based on 6-rectangle"""


class Rectangle:
    """Defines a rectangle"""
    number_of_instances = 0
    print_symbol = '#'

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        else:
            return (self.height * 2) + (self.width * 2)

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        elif isinstance(self.print_symbol, str):
            return (str(self.print_symbol) * self.width + '\n') * self.height
        elif hasattr(self.print_symbol, '__iter__'):
            return ''.join(
                [str(self.print_symbol) * self.width + '\n'] * self.height
            )

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
