#!/usr/bin/python3
"""Defines a class -> Rectangle.
Returns its area and perimeter
"""


class Rectangle:
    """Rectangle class."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.
        Args:
            width (int): rectangle width
            height (int): rectangle height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
