#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    else:
        element = my_list[idx]
        my_list.remove(element)
        return my_list
