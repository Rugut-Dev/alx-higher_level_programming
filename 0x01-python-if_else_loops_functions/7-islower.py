#!/usr/bin/python3
def islower(c):
    for i in c:
        if ord(i) >= 97 and ord(i) <= 122:
            return True
        else:
            return False
