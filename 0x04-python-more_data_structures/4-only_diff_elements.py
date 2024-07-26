#!/usr/bin/python3
"""returns a set of all elements present in only one set."""


def only_diff_elements(set_1, set_2):
    """returns a set of all elements present in only one set."""

    set_r = [i for i in set_1 for j in set_2 if i == j]
    set_t = set_1 | set_2
    i = 0
    while (i < len(set_r)):
        set_t.remove(set_r[i])
        i += 1
    return set_t
