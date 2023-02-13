#!/usr/bin/python3
"""Defines unittests for models/rectangle.py.
Unittest classes:
    TestRectangle_instantiation 
    TestRectangle_width 
    TestRectangle_height 
    TestRectangle_x
    TestRectangle_y 
    TestRectangle_order_of_initialization 
    TestRectangle_area 
    TestRectangle_update_args 
    TestRectangle_update_kwargs 
    TestRectangle_to_dictionary 
"""
import unittest

from models.base import Base
from models.rectangle import Rectangle

class TestRec(unittest.TestCase):
    def test_instance(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_noid(self):
        ri = Rectangle(10,2)
        self.assertEqual(1,ri.id)

        r2 = Rectangle(2,10)
        self.assertEqual(2,r2.id)
    
    def test_id(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(12,r3.id)
    
    def test_width(self):
        r = Rectangle(10,2)
        with self.assertRaises(ValueError) as e:
            r.width = -10
            self.assertEqual("width must be >= 0",str(e.exception))

    def test_height(self):
        r = Rectangle(10,2)
        with self.assertRaises(ValueError) as e:
            r.height = -10
            self.assertEqual("height must be >= 0",str(e.exception))

    def test_width(self):
        r = Rectangle(10,2)
        with self.assertRaises(ValueError) as e:
            r.x = -10
            self.assertEqual("x must be >= 0",str(e.exception))
    
    def test_width(self):
        r = Rectangle(10,2)
        with self.assertRaises(ValueError) as e:
            r.y = -10
            self.assertEqual("y must be >= 0",str(e.exception))
    
    def test_int_width(self):
        r = Rectangle(10,2)
        self.assertIsInstance(r.width, int)
    
    def test_int_width(self):
        r = Rectangle(10,2)
        self.assertIsInstance(r.height, int)

    def test_int_width(self):
        r = Rectangle(10,2,6)
        self.assertIsInstance(r.x, int)

    def test_int_width(self):
        r = Rectangle(10,2,0,5)
        self.assertIsInstance(r.y, int)

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(6,r1.areaa())

    def test_area_all(self):
        rec = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(56,rec.area())

    def test_display(self):
        rec = Rectangle(4, 6)
        expected = "####\n####\n####\n####\n####\n####"
        result = rec.display()
        self.assertEqual(expected,result)
    
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        expected = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(expected,r1)

    def test_str_short(self):
        r2 = Rectangle(5, 5, 1)
        expected = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(expected,r2)

    def test_update_one(self):
        r1 = Rectangle(10, 10, 10, 10)
        new = "[Rectangle] (89) 10/10 - 10/10"
        self.assertEqual(new, r1.update(89))

    def test_update_many(self):
        r1 = Rectangle(10, 10, 10, 10)
        new = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(new, r1.update(89, 2, 3, 4, 5))

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        new = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(new, r1.update(x=1, height=2, y=3, width=4))

    def test_dict(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()
        result = "{'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10}"
        self.assertEqual(result,r1_dictionary)

    def test_type(self):
        r2 = Rectangle(1, 1)
        r2_type= type(r2.to_dictionary())
        result = "<class 'dict'>"
        self.assertEqual(result,r2_type)
