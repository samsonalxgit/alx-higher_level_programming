#!/usr/bin/python3
"""contains a function to add two integers"""


def add_integer(a, b=98):
    """function that returs an integer
    args:
        a (int or float): first param
        b (int or float): second param
    Raises TypeError with corresponding message if a or b
    isn't an int or a float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
