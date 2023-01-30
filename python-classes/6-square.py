#!/usr/bin/python3
'''defines a square'''


class Square:
    '''creates a square'''
    def __init__(self, size=0, position=(0, 0)):
        '''initializes a square with side of square'''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''gets the size of the square'''
        return self._Square__size

    @size.setter
    def size(self, value):
        '''sets the size of the square'''
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self._Square__size = value

    @property
    def position(self):
        '''return the square position'''
        return self._Square__position

    @position.setter
    def position(self, value):
        '''sets the position of the square'''
        if isinstance(value, tuple) is False or len(value) != 2 or\
           isinstance(value[0], int) is False or\
           isinstance(value[1], int) is False or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self._Square__position = value

    def area(self):
        '''return the square area'''
        return self._Square__size ** 2

    def my_print(self):
        '''prints the square according to its position'''
        if self._Square__size == 0:
            print()
        else:
            if self._Square__position[1] > 0:
                print("\n" * self._Square__position[1], end="")
            for i in range(self._Square__size):
                print(" " * self._Square__position[0], end="")
                print("#" * self._Square__size)
