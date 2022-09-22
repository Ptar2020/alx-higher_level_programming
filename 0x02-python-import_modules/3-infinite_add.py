#!/usr/bin/python3
from sys import argv


def getSum():
    argSum = 0
    for item in argv[1:]:
        argSum = argSum + int(item)
    print(argSum)


if __name__ == "__main__":
    getSum()
