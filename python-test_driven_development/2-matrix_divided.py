#!/usr/bin/python3
"""module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """returns a new matrix with all elements divided by div"""
    row = 0
    number = 0

    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if isinstance(div, int) is False and isinstance(div, float) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    size = len(matrix[row])
    for row in matrix:
        for number in row:
            if size != len(row):
                raise TypeError("Each row of the matrix must have the same size")

            if type(number) is not int and type(number) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(number / div, 2) for number in row] for row in matrix]
