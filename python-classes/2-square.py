#!/usr/bin/python3
'''defines a square'''


class Square:
    '''defines a square with size'''
    def __init__(self, size=0):
        self._Square__size = size

        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
