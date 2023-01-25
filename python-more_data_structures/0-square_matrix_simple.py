#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if not matrix:
        print()
    else:
        sq_list = [[number ** 2 for number in row] for row in matrix]
        return sq_list
