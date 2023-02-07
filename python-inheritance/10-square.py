#!/usr/bin/python3
"""module for subclass Square"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """subclass square that inherits from Rectangle""" 
    def __init__(self, size):
        self.__size = size
        super().__init__(self.__size, self.__size)
    
    def area(self):
        return self.__size * self.__size

