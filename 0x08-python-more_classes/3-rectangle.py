#!/usr/bin/python3
"""
This module defines a class - Rectangle
"""


class Rectangle:
    """
    This class has two attributes, width and height
    both will have property and setter function definition
    """

    def __init__(self, width=0, height=0):
        """
        This instantiates width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Function to return width if setter checks have passed
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        The setter validates if value is >= 0
        Raises: TypeError and ValueError
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def length(self):
        """This function returns the length if the setter check are passed
        """
        return self.__length

    @length.setter
    def length(self, value):
        if not isinstance(value, int):
            raise TypeError("length must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__length = value

    def area(self):
        """Return area of a rectangle given length and width"""
        return (self.length * self.length)
    
    def perimeter(self):
        """Returns perimeter given length and width"""
        if self.length == 0 or self.width == 0:
            return 0
        return ((self.length + self.width) * 2)
    
    def __str__(self):
        """
        Returns string of Rectangle using #
        if 0 returns empty string
        """
        if self.width == 0 or self.height == 0:
            return ("")
        width = "#" * self.width
        rectangle = width
        for x in range(self.height - 1):
            rectangle += "\n" + width
        return (rectangle)
