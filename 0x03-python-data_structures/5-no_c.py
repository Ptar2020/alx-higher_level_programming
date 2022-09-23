#!/usr/bin/env python3

def no_c(my_string):
    for char in my_string:
        if char not in 'Cc':
            print(char, end="")


if __name__ == "__main__":
    no_c()
