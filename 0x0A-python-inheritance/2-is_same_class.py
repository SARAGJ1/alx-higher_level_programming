#!/usr/bin/python3
"""the object is exactly an instance of the specified class"""


def is_same_class(obj, a_class):
    """func that check if the object is of a_class"""

    if dir(obj) == dir(a_class):
        return True
    else:
        return False
