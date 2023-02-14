#!/usr/bin/python3
""" Unittest for Base
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_no_args(self):
        self.assertEqual(Base().id, 1)
    
    def test_next(self):
        self.assertEqual(Base().id, 2)

    def test_id(self):
        self.assertEqual(Base(89).id, 89)

    def test_to_json_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

if __name__ == '__main__':
    unittest.main()