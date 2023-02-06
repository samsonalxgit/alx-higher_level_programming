#!/usr/bin/python3
""" A function that returns same class or inherit from a class """


def is_kind_of_class(obj, a_class):
    """
    Return true if the object is an instance of a class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
