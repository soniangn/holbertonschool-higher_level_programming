#!/usr/bin/python3
"""module that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """returns a new matrix with all elements divided by div"""
    row = 0
    number = 0
    new_matrix = []

    if range(len(matrix)) != range(len(matrix[row])):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int or type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
            
    for row in range(len(matrix)):
        for number in range(len(matrix[row])):
            if type(matrix[row][number]) is not int or\
               type(matrix[row][number]) is not float:
               raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix.append(round((matrix[row][number] / div), 2))
    return new_matrix