#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


def calculator():
    args = len(argv[1:])
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        if argv[2] == "+":
            print("{} {} {} = {}".format(int(argv[1]), argv[2], int(
                argv[3]), add(int(argv[1]), int(argv[3]))))
        elif argv[2] == "-":
            print("{} {} {} = {}".format(int(argv[1]), argv[2], int(
                argv[3]), sub(int(argv[1]), int(argv[3]))))
        elif argv[2] == "/":
            print("{} {} {} = {}".format(int(argv[1]), argv[2], int(
                argv[3]), div(int(argv[1]), int(argv[3]))))
        elif argv[2] == "*":
            print("{} {} {} = {}".format(int(argv[1]), argv[2], int(
                argv[3]), mul(int(argv[1]), int(argv[3]))))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    calculator()
