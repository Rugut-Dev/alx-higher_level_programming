#!/usr/bin/python3

def search_replace(my_list, search, replace):
    if my_list:
        for i in my_list:
            new_list = list(map(lambda i: replace if i == search else i, my_list))

    return new_list
