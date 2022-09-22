#!/usr/bin/python3
def add(a, b):
    """My addition function

    Args:
        a (int): first integer
        b (int): second integer
    
    Returns:
        The return value. a + b
    """
    result = a + b
    return (result)
a = 10
b = 5
print(f"1.{a} + {b} = {add(a, b)}")
print("2.{0} + {1} = {2}".format(a, b, add(a, b)))