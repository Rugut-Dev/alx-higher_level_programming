#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary:
        max_val_key = max(a_dictionary, key=a_dictionary.get)
        return max_val_key
    else:
        return None
