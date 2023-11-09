#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_listof_lists = matrix.copy()
    squared_lst = []

    for lst in new_listof_lists:
        for i in lst:
            sq = list(map(lambda i : i * i, lst))
        squared_lst.append(sq)

    return squared_lst
