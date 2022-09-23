#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for item in my_list:
        print("{}".format(item), end="\n")


if __name__ == "__main__":
    print_list_integer()
