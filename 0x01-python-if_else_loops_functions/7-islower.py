#!/usr/bin/python3
def islower(c):
    if 'a' <= c <= 'z' and len(c) != 0:
        return True
    elif 'A' <= c <= 'Z' and len(c) != 0:
        return False
