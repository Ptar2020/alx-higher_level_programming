#!/usr/bin/python3
"""
Program rints the ASCII alphabet, in lowercase, not followed by a new line.

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store characters in a variable
You are not allowed to import any module
"""

for letter in range(ord('a'), ord('z') + 1):
    print("{:c}" .format(letter), end="")  # default for end='\n'