#!/usr/bin/python3
""" Module for pascal_triangle method """


def pascal_triangle(n):
    """returns a list of lists of integers """
    """representing the Pascal s triangle of n"""
    if n <= 0:
        return []

    new_list = [[] for i in range(n)]

    new_list[0].append(1)
    if n > 1:
            new_list[1] = [1, 1]

    if n > 2:
        for row in range(2, n):
            new_list[row].append(1)
            for i in range(row - 1):
                new_list[row].append(new_list[row - 1][i] +
                                     new_list[row - 1][i + 1])
            new_list[row].append(1)
    return new_list
