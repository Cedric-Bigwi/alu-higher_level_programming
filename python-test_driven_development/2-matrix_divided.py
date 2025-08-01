#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number and
    returns a new matrix.

    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.

    Returns:
        A new matrix with all elements divided by div and rounded
        to 2 decimals.
    """
    if not isinstance(matrix, list) or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    row_lengths = [len(row) for row in matrix]
    if row_lengths and any(length != row_lengths[0] for length in row_lengths):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
