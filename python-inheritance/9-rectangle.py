#!/usr/bin/python3
"""Module for subclass Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializes rectangle instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """return rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """return rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
