#!/usr/bin/python3

def no_c(my_string):
    string_list = []
    new_string = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            pass
        else:
            string_list.append(i)
    for elem in string_list:
        new_string += elem
    return new_string
