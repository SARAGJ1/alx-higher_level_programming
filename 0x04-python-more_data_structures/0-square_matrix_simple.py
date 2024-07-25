#!/usr/bin/python3
"""function that computes the square value of all integers of a matrix."""


def square_matrix_simple(matrix=[]):
    """function that computes the square value of all integers of a matrix."""

    return [[elem ** 2 for elem in row] for row in matrix]
