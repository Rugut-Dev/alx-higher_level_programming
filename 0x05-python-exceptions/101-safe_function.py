#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as err:
        sys.stderr.write(f"Exception: {err}\n")
        return None
    else:
        return res
