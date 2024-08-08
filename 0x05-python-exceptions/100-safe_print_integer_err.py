#!/usr/bin/python3
"""function that prints an integer."""


def safe_print_integer_err(value):
    """function that prints an integer."""

    try:
        print("{:d}".format(value))
        return True
    except:
        print("Exception: Unknown format code 'd' for object of type 'str'")
        return False
