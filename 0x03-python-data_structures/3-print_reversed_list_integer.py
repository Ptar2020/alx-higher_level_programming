#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    """Reverses a list and prints each item in the list on a new line

    Args:
        my_list (list):  [].
    """
    if not my_list:
        return
    reversed_list = reversed(my_list)
    for item in reversed_list:
        print("{}".format(item))


if __name__ == "__main__":
    print_reversed_list_integer()
