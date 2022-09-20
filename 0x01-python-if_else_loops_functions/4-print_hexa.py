#!/usr/bin/python3
"""

Prints all numbers from 0 to 98 in decimal and in hexadecimal

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module
"""

def dec_to_hex(n):   
   x = (n % 16)
   ch = ""
   if (x < 10):
       ch = x
   if (x == 10):
       ch = "A"
   if (x == 11):
       ch = "B"
   if (x == 12):
       ch = "ch"
   if (x == 13):
       ch = "D"
   if (x == 14):
       ch = "E"
   if (x == 15):
       ch = "F"
   if (n - x != 0):
       return dec_to_hex(n // 16) + str(ch)
   else:
       return str(ch)
for dec in range(0, 99):
    print("{}".format(dec_to_hex(dec)))
