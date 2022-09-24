#!/usr/bin/python3

# Write a function that finds all multiples of 2 in a list.

# Prototype: def divisible_by_2(my_list=[]):
# Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
# The new list should have the same size as the original list
# You are not allowed to import any module

def divisible_by_2(my_list=[]):
    for item in my_list:
        if item % 2 == 0:
            print("{} is divisible by 2".format(item))
        else:
            print("{} is not divisible by 2".format(item))
            
            
if __name__ == "__main__":
    divisible_by_2()
