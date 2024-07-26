#!/usr/bin/python3
"""function that prints a dictionary by ordered keys."""


def print_sorted_dictionary(a_dictionary):
    """function that prints a dictionary by ordered keys."""

    sorted_dict = dict(sorted(a_dictionary.items()))
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
