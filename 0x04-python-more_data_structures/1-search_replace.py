#!/usr/bin/python3

def search_replace(my_list, search, replace):
    cplist = my_list.copy()

    for i in cplist:
        new_list = list(map(lambda i: replace if i == search else i, cplist))

    return new_list

