#!/usr/bin/python3
"""
Write a function that prints the numbers from 1 to 100 separated by a space.

For multiples of three print Fizz instead of the number
For multiples of five print Buzz.
For numbers which are multiples of both three and five print FizzBuzz.
Prototype: def fizzbuzz():
Each element should be followed by a space
You are not allowed to import any module
You don’t need to understand __import__
"""


def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0:
            if number % 5 == 0:
                print("{}".format("FizzBuzz"), end=" ")
            else:
                print("{}".format("Fizz"), end=" ")
        elif number % 5 == 0:
            if number % 3 == 0:
                print("FizzBuzz", end=" ")
            else:
                print("Buzz", end=" ")
        else:
            print("{}".format(number), end=" ")
