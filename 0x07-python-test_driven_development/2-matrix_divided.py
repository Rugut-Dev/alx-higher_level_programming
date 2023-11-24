#!/usr/bin/python3
"""Division of matrix elems

Divides all elements of a matrix, ensuring that matrix is indeed a list of \
lists of integers or floats. Afterwards, it rounds off the result to two \
decimal places"""


def matrix_divided(matrix, div):
    """ Matrix_divided function checks for correctness of inputs and raises\
various exceptions when not"""
    if not isinstance(matrix, list) or \
       all(not isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if row_len != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, int) and not isinstance(elem, float):
                raise TypeError("matrix must be a matrix (list of \
lists) of integers/floats")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round((elem / div), 2) for elem in row] for row in matrix]

    return new_matrix
