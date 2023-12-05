#!/usr/bin/python3
"""Prints lines of a file"""


def read_file(filename=""):
    """prints lines in f"""
    with open(filename, mode='r',  encoding="utf-8") as f:
        for line in f:
            print(line, end='')
