#!/usr/bin/python3
"""Python bytecode:"""


def magic_calculation(a, b):
    """Python bytecode:"""

    result = 0
    try:
        for i in range(1, 3):
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
    except Exception:
        result = b + a
        break
    return result
