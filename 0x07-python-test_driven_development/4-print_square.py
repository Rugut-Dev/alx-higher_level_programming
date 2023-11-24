#!/usr/bin/python3
"""Print_Square

prints a square of size 'size' using #"""


def print_square(size):
    """print_square

checks the value of size and raises an exception where needed
finally prints the square after all cases are satisfied"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()
