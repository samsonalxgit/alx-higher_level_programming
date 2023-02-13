#!/usr/bin/python3>
"""Defines unittests for models/square.py.
Unittest classes:
    TestSquare_instantiation 
    TestSquare_size 
    TestSquare_x  
    TestSquare_y 
    TestSquare_order_of_initialization
    TestSquare_area
    TestSquare_stdout
    TestSquare_update_args
    TestSquare_update_kwargs
    TestSquare_to_dictionary
"""

import unittest
from models.base import Base

from models.square import Square

class TestSquare(unittest.TestCase):
    def test_inst(self):
         self.assertIsInstance(Square(2,2), Base)

    def test_inheritance(self):
        s1 = Square(5)
        answer = "[Square] (1) 0/0 - 5"
        self.assertEqual(answer,s1)
        area = 25
        self.assertEqual(area,s1.area)
        display ="#####\n#####\n#####\n#####\n#####"
        self.assertEqual(display, s1.display())

    def test_second(self):
        s3 = Square(3, 1, 3)
        answer = "[Square] (3) 1/3 - 3"
        self.assertEqual(answer,s3)
        area = 9
        self.assertEqual(area,s3)
        display = "###\n###\n###"
        self.assertEqual(display,s3)

    def test_setter(self):
        s1 = Square(5)
        with self.assertRaises(TypeError) as e:
            s1.size = "9"
            self.assertEqual("width must be an integer",e.exception)

    def test_args(self):
        s1 = Square(size=7, id=89, y=1)
        result = "[Square] (89) 12/1 - 7"
        self.assertEqual(result,s1)

    def test_dict(self):
        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        result = "{'id': 1, 'x': 2, 'size': 10, 'y': 1}"
        self.assertEqual(result,s1_dictionary)

    def test_cls(self):
        s1 = Square(10, 2, 1)
        s1_type = type(s1.to_dictionary())
        rsl = "<class 'dict'>"
        self.assertEqual(rsl,s1_type)
