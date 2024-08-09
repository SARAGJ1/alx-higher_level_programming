#!/usr/bin/python3
"""function that executes a function safely."""

import sys
def safe_function(fct, *args):
    """function that executes a function safely."""

    try:
        x = fct(*args)
        return x
    except (IndexError, ArithmeticError) as e:
        print("Exception:", e, file=sys.stderr)
        return None
