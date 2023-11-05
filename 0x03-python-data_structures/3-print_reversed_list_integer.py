#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = []
    for i in my_list:
        rev_list.append(i)

    rev_list.reverse()
    for elem in rev_list:
        print("{:d}".format(elem))
#    my_list.reverse()
#    for i in my_list:
#        print("{:d}".format(i))
