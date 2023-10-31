#!/usr/bin/python3
def uppercase(str):
    uppercase_text = ""
    for i in str:
        if 'a' <= i <= 'z':
            uppercase_i = chr(ord(i) - 32)
            uppercase_text += uppercase_i
        else:
            uppercase_text += i
    print("{}".format(uppercase_text))
