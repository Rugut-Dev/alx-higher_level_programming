#!/usr/bin/python3

def search_replace(my_list, search, replace):
    for i in my_list:
        n_list = list(map(lambda i: replace if i == search else i, my_list))

    return n_list
