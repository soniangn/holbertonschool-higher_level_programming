#!/usr/bin/python3
"""module for Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ creates an instance of Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
    
    @property
    def size(self):
        """ gets the size of the square"""
        return self.width
    
    @size.setter
    def size(self, value):
        """ validates value and assigns width and height to value """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
