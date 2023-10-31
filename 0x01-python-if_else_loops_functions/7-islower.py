#!/usr/bin/python3
def islower(c):
    for i in c:
        if 'a' <= i <= 'z':
            return True
        elif 'A' <= i <= 'Z':
            return False
