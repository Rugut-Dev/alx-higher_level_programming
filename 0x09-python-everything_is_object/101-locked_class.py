#!/usr/bin/python3
"""LockedClass
prevents the user from dynamically creating new instance attributes,
except if the new instance attribute is called first_name.
"""


class LockedClass:
    """checks for 'firstname'"""
    __slots__ = ('first_name',)

    def __setattr__(self, attr, value):
        if hasattr(self, attr) and attr != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(attr))
        super().__setattr__(attr, value)
