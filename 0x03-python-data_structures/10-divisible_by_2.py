#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if not my_list:
        return
    else:
        new_list = [n % 2 == 0 for n in my_list]
    return new_list


if __name__ == "__main__":
    divisible_by_2()
