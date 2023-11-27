#!/usr/bin/python3
"""text_indentation
prints a text with 2 new lines after each of chars in search_chars"""


def text_indentation(text):
    """Checks for errors,and prints two new lines as expected"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    search_chars = ['?', ':', '.']
    for i in range(len(text)):
        if text[i] in search_chars:
            print(text[i], end='')
            print('\n\n', end='')
        elif text[i - 1] in search_chars and text[i] == ' ':
            pass
        else:
            print(text[i], end='')
