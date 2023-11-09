#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    a_dict = {key: value * 2 for key, value in a_dictionary.items()}

    return a_dict
