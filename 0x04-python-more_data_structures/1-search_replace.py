#!/usr/bin/python3

def search_replace(my_list, search, replace):
    list_copy = my_list.copy()

    for i in list_copy:
        new_list = list(map(lambda i: replace if i == search else i, list_copy))

    return new_list
