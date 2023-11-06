#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2 or len(tuple_b) < 2:
        tuple_0 = (0,) * (2 - len(tuple_a))
        tuple_a += tuple_0
        a, b = tuple_a

        tuple_02 = (0,) * (2 - len(tuple_b))
        tuple_b += tuple_02
        c, d = tuple_b

    elif len(tuple_a) > 2 or len(tuple_b) > 2:
        a, b, *rest_of_tuple = tuple_a
        del rest_of_tuple

        c, d, *rest_of_tuple_b = tuple_b
        del rest_of_tuple_b
    else:
        a, b = tuple_a
        c, d = tuple_b

    res_tuple = a + c, b + d
    return res_tuple
