#!/usr/bin/python3
import math


class MagicClass:
    """ class that creates a circle area"""

    def __init__(self, radius=0):
        """ Initialization first """
        self.__radius = 0
        if not isinstance(radius, int) and not isinstance(radius, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ Works out the area """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ The function defining the circumference """
        return ((2 * math.pi) * self.__radius)
