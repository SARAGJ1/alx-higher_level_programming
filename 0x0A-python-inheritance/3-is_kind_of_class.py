#!/usr/bin/python3
'''Module for is_same_class method.'''


def is_kind_of_class(obj, a_class):
    """check if the object is instance of the class"""

    if isinstance(obj, a_class):
        return True
    return False
