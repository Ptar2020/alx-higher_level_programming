#!/usr/bin/python3

def no_c(my_string):
    return my_string.translate({ord(c): None for c in "cC"})


if __name__ == "__main__":
    no_c()
