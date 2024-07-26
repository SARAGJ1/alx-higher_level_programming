#!/usr/bin/python3
"""returns a new dictionary with all values multiplied by 2"""


def multiply_by_2(a_dictionary):
    """returns a new dictionary with all values multiplied by 2"""

    new_dic = a_dictionary.copy()
    for key, value in new_dic.items():
        new_dic[key] = value * 2
    return new_dic
