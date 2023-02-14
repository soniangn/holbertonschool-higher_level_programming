#!/usr/bin/python3
""" Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_rectangle_1(self):
        obj = Rectangle(1, 2)
        self.assertEqual(obj.id, 1)
    
    def test_rectangle_2(self):
        obj = Rectangle(1, 2, 3)
        self.assertEqual(obj.id, 2)

    def test_rectangle_3(self):
        obj = Rectangle(1, 2, 3, 4)
        self.assertEqual(obj.id, 3)
    

if __name__ == '__main__':
    unittest.main()