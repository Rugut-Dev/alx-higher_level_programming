#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) < 1:
        str_len = len(sentence)
        res_tuple = str_len, None
    else:
        str_len = len(sentence)
        res_tuple = str_len, sentence[0]

    return res_tuple
