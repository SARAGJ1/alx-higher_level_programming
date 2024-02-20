#!/usr/bin/python3
'''Module for is_same_class method.'''


def inherits_from(obj, a_class):
    """func to ckeck if a class is inhirited from another"""

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
