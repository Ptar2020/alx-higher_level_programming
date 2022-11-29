#!/usr/bin/python3
"""A rectangle class that inherits from a Base class"""
from models import base


class Rectangle(base.Base):
    """The rectangle class that inherits from the Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Instantiating the class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Gets the width value"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """Validates the width value"""
        if value <= 0:
            raise ValueError("width must be > 0")
        if type(value) is not int:
            raise TypeError("width must be an integer")
        self.__width = value

    @property
    def height(self):
        """Gets the height value"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Gets the x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Sets the x value"""
        if value < 0:
            raise ValueError("x must be >= 0")
        if type(value) is not int:
            raise TypeError("x must be an integer")
        self.__x = value

    @property
    def y(self):
        """Gets the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Validates the value of y"""
        if value < 0:
            raise ValueError("y must be >= 0")
        if type(value) is not int:
            raise TypeError("y must be an integer")
        self.__y = value

    def area(self):
        """This method returns the area of a rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """
        This function prints in stdout the rectangle
        """
        print(("\n" * self.__y) + "\n".join(((" " * self.__x) +
                                             ("#" * self.__width))
                                            for a in range(self.__height)))

    def __str__(self):
        """
        This function returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return ("[Rectangle] ({}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y, self.__width,
                       self.__height))

    def update(self, *args, **kwargs):
        """
        function assigns an argument to each attribute
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.width = j
                if i == 2:
                    self.height = j
                if i == 3:
                    self.x = j
                if i == 4:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        This function returns the dictionary representation
        of a rectangle
        """
        dict = {}
        dict["id"] = self.id
        dict["width"] = self.width
        dict["height"] = self.height
        dict["x"] = self.x
        dict["y"] = self.y
        return (dict)
