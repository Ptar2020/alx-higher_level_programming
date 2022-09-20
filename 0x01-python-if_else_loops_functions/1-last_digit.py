#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
   last = number % 10
else:
   last = int(repr(number)[-1] ) * -1
print("Last digit of {0} is {1}".format(number, last), end = " ")
if last > 5:
   print(f"and is greater than 5")
elif last == 0:
   print(f"and is 0")
else:
   print(f"and is less than 6 and not 0")
