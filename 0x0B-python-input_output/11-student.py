#!/usr/bin/python3
""" creating student class """


class Student:
    """ Defining a class"""
    def __init__(self, first_name, last_name, age):
        """ Initializing a class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dictionary representation """
        if (type(attrs)) == list and all(type(i) == str for i in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """update all the attributtes of student"""
        for i in json:
            self.__dict__.update({i: json[i]})
