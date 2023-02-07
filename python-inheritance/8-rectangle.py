#!/usr/bin/python3
"""Module for class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """initializes rectangle instance"""
        if self.integer_validator("width", width):
            self.width = width
        if self.integer_validator("height", height):
            self.height = height
