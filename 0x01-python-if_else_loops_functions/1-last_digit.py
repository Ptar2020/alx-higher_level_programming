#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

last = number % 10
if last > 5:
   print("Last digit of {0} is {1} and is less than {2} and not 0".format(number, last, 5))