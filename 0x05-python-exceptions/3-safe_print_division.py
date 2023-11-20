#!/usr/bin/python3

def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
    except (UnboundLocalError, ZeroDivisionError):
        res = None
        return None
    else:
        return res
    finally:
        print("Inside result: {}".format(res))
