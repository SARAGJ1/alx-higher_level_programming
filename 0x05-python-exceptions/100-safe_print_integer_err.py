#!/usr/bin/python3
"""function that prints an integer."""

import sys
def safe_print_integer_err(value):
    """function that prints an integer."""

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        print("Exception:", e, file=sys.stderr)
        return False
