#!/usr/bin/python3
"""module for BaseGeometry"""

class BaseGeometry:
    """integer validator"""
    def area(self):
        """raise Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise TypeError("<name> must be greater than 0")
