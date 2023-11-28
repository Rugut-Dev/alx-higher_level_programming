#!/usr/bin/python3
"""
prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name.
"""


class LockedClass:
    """checks for 'firstname'"""
    def __setattr__(self, attr, value):
        if attr != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(attr))
        else:
            super().__setattr__(attr, value)
