#!/usr/bin/env python3

if __name__ == "__main__":
    def no_c(my_string):
        for char in my_string:
            if char not in 'Cc':
                print(char, end="")
