#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for elem in i:
            print("{:d}".format(elem), end=" ")
        print()
