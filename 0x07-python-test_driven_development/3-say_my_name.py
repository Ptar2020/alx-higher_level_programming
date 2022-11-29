#!/usr/bin/python3
"""
This is a function that prints 'My name is <first name> <last name>'
first_name and last_name must be strings otherwise, raises a TypeError exception
"""


def say_my_name(first_name, last_name=""):
    """Prints a concatenation of first and last names

    Args:
        first_name (string): The first name
        last_name (str, optional): The last name. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
