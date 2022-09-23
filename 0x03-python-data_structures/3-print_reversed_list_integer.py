#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    reversed_list = my_list.reverse()
    for item in reversed_list:
        print("{}".format(item), end="\n")


if __name__ == "__main__":
    print_reversed_list_integer()
