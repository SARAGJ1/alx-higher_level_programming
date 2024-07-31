#!/usr/bin/python3
"""function that returns the weighted average of all integers tuple"""


def weight_average(my_list=[]):
    """function that returns the weighted average of all integers tuple"""

    if my_list == []:
        return 0
    r = 0
    sum = 0
    i = 0
    while i < len(my_list):
        r = r + (my_list[i][0] * my_list[i][1])
        sum = sum + my_list[i][1]
        i = i + 1
    return r / sum
