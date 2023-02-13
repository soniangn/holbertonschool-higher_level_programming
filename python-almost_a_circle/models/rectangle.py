#!/usr/bin/python3
"""module for Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """class for creating a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if isinstance(x, int):
            if x < 0:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError("x must be an integer")
        if isinstance(y, int):
            if y < 0:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError("y must be an integer")

    @property
    def width(self):
        """gets the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width and validates that width is a positive integer"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height and validates that height is a positive integer"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets x"""
        return self.__x

    @x.setter
    def x(self, value):
        """validates and sets x"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError('x must be >= 0')
        else:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """gets y"""
        return self.__y

    @y.setter
    def y(self, value):
        """validates and sets y"""
        if isinstance(value, int):
            if value < 0:
                raise ValueError('y must be >= 0')
        else:
            raise TypeError("y must be an integer")
        self.__y = value

    def area(self):
        """returns the value of the Rectangle instance area"""
        return self.__height * self.__width

    def display(self):
        """prints in stoud the rectangle instance with """
        """ character # """
        if self.__y:
            print("\n" * self.__y, end="")

        for character in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """ overrides the __str__ method """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """ updates the rectangle """
        length = len(args)
        if length > 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return vars(self)
