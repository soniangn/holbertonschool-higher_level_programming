#!/usr/bin/python3
"""module for Rectangle class"""
from base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    @property
    def width(self):
        """gets the width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """sets the width"""
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """sets the height"""
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """sets x"""
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """sets y"""
        self.__y = value
