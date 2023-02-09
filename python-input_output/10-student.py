#!/usr/bin/python3
""" Module for class Student """


class Student:
    """ defines a student """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        for attr in attrs:
            if type(attr) is not str:
                return self.__dict__
        return {attr: self.__dict__[attr] for attr
                in self.__dict__ if attr in attrs}
