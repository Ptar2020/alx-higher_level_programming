#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list or len(my_list) == 0:
        return None
    else:
        return sorted(my_list)[-1]


if __name__ == "__main__":
    max_integer()
