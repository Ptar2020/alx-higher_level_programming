#!/usr/bin/python3
"""
Checks for lowercase character.

Prototype: def islower(c):
Returns True if c is lowercase
Returns False otherwise
You are not allowed to import any module
You are not allowed to use str.upper() and str.isupper()
Tips: ord()
You don’t need to understand __import__
"""

def islower(c):
    if ord(c) > 96 and ord(c) < 123:
        return True
    return False

