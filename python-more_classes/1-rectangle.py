#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """defines a rectangle by its width and height"""
    def __init__(self, width=0, height=0):
        """initializes the rectangle"""
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """gets the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if isinstance(value, int) is False: 
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """gets the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height of the rectangle"""
        if isinstance(value, int) is False: 
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

