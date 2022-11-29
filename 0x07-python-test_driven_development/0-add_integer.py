#!/usr/bin/python3
"""
    This module takes two values , gets their sum and returns it
    Both values must be either float or integer
    The returned sum is cast to integer
    Values other than integer or float return TypeError.
"""


def add_integer(a, b=98):
    """Works out the sum of two values and returns it"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
