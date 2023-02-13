#!/usr/bin/python3
"""Unittest classes:
    TestBase_instantiation 
    TestBase_to_json_string 
    TestBase_save_to_file 
    TestBase_from_json_string 
    TestBase_create 
    TestBase_load_from_file 
    TestBase_save_to_file_csv 
    TestBase_load_from_file_csv 
"""
import unittest

from models.base import Base
from models.rectangle import Rectangle

"""
testing the base class method
this is the main class that all the other class inherit from 
"""
class TestBase(unittest.TestCase):
    """
    Adding test to check if it icrements as it goes
    """
    def test_add(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id,b1.id + 1)
        b3 = Base()
        self.assertEqual(b3.id,b2.id + 1)

    def test_val(self):
        b4 = Base(12)
        self.assertEqual(12,b4.id)

    def test_tostring(self):
        r1 = Rectangle(10, 7, 2, 8)
        dict = r1.to_dictionary()
        json_dictionary = type(Base.to_json_string([dict]))
        str = type("[{x: 2, width: 10, id,: 1, height: 7, y : 8}]")
        self.assertEqual(str, json_dictionary)

    def save_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        out = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        with open("Rectangle.json", "r") as file:
            self.assertEqual(out,file.read)

    def test_json_to_dict(self):
        list_input = [
        {'id': 89, 'width': 10, 'height': 4}, 
        {'id': 7, 'width': 1, 'height': 7}
        ]
        jstr = Rectangle.to_json_string(list_input)
        jdict = Rectangle.from_json_string(jstr)
        out = "[<class 'list'>] [{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}]"
        self.assertEqual(out,jdict)
    
    def test_dictoinst(self):
        r1 = Rectangle(3, 5, 1)
        to_dic = r1.to_dictionary()
        r2 = Rectangle.create(**to_dic)
        self.assertIsNot(r1,r2)
        self.assertEqual(r1,r2)

    def test_rec(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(len(list_rectangles_input),len(list_rectangles_output))
