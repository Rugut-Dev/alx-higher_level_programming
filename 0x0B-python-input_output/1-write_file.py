#!/usr/bin/python3
"""func that writes a string to a textfile and
returns the no. of chars written"""


def write_file(filename="", text=""):
    """returns no. of chars"""
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
