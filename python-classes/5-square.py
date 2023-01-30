#!/usr/bin/python3
'''defines a square'''


class Square:
    '''creates a square'''
    def __init__(self, size=0):
        '''initializes a square with side of square'''
        self._Square__size = size

    @property
    def size(self):
        '''gets the size of the square'''
        return self._Square__size

    @size.setter
    def size(self, new_size):
        '''sets the size of the square'''
        if isinstance(new_size, int) is False:
            raise TypeError("size must be an integer")
        elif new_size < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = new_size

    def area(self):
        '''return the square area'''
        return self._Square__size ** 2

    def my_print(self):
        if self._Square__size == 0:
            print()
        else:
            for i in range(self._Square__size):
                    print("#" * self._Square__size)
