#!/usr/bin/python3
"""module for Square class"""
from rectangle import Rectangle


class Square(Rectangle):
    """ creates an instance of Square that inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes a square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)
