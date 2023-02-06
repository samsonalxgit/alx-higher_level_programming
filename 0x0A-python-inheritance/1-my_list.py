#!/usr/bin/python3

""" Crating Mylist class """


class Mylist(list):
    """
    Mylist class that inherit list
    """
    def print_sorted(self):
        """
        prints the list in sorted order
        """
        print(sorted(self))
