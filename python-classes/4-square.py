#!/usr/bin/python3
'''defines a square'''


class Square:
    '''defines a square with size'''
    def __init__(self, size=0):
        self._Square__size = size

    @property
    def size(self):
        return self._Square__size
    
    @size.setter
    def size(self, new_size):
        if isinstance(new_size, int) is False:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = new_size

    def area(self):
        return self._Square__size ** 2
