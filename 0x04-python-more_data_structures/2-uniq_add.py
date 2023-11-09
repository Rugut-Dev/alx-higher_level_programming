#!/usr/bin/python3

def uniq_add(my_list=[]):
    my_set = set(my_list)
    res = 0

    for i in my_set:
        res += i

    return res
