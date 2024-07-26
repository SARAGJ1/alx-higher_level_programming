#!/usr/bin/python3
"""function that adds all unique integers in a list"""


def uniq_add(my_list=[]):
    """function that adds all unique integers in a list"""

    summ = 0
    i = 0
    while (i < len(my_list)):
            if (my_list.count(my_list[i]) == 1):
                summ = summ + my_list[i]
            i += 1
    return summ
