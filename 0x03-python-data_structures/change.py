#!/usr/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the solve function below.
uppers = string.ascii_uppercase
lowers = string.ascii_lowercase
def solve(s):
    for char in s:
        if char == s[0]:
            char.upper()
            print(char)
solve("james oduor")