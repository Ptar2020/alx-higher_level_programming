#!/usr/bin/python3
"""
Write a function that prints a string in uppercase followed by a new line.

Prototype: def uppercase(str):
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand __import__
"""


def uppercase(str):
    tmp = list(str)
    for i in range(len(tmp)):
        if (ord(tmp[i]) > 96 and ord(tmp[i]) < 123):
            tmp[i] = chr(ord(tmp[i]) - 32)
    print("{}".format(("").join(tmp)))
