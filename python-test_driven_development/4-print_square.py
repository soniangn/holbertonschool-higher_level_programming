#!/usr/bin/python3
""" module with function print_square(size) """


def print_square(size):
    """prints a square with the character #"""
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) is True and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
