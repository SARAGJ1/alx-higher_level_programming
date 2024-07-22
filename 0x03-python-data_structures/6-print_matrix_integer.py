#!/usr/bin/python3
"""function that prints a matrix of integers."""


def print_matrix_integer(matrix=[[]]):
    """function that prints a matrix of integers."""

    for row in matrix:
        for i, elem in enumerate(row):
            if i != 0:
                print(" ", end="")
                print("{:d}".format(elem), end="")
        print()
