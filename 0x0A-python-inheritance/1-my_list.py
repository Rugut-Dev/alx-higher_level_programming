#!/usr/bin/python3
"""Class inheritting from list"""


class MyList(list):
    """returns sorted list"""
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

    def __init__(self):
        super().__init__()
