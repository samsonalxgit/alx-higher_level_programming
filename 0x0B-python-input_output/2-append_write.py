#!/usr/bin/python3
"""Appends a string of a text file"""


def append_write(filename="", text=""):
    """Appends a string of a text file"""
    with open(filename, 'a') as f:
        return f.write(text)
