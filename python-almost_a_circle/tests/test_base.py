#!/usr/bin/python3
""" Unittest for Base
"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_no_args(self):
        self.assertEqual(Base(), 1)
    
    def test_next(self):
        self.assertEqual(Base(), 1)

    def test_id(self):
        self.assertEqual(Base(89), 89)

    def test_to_json(self):
        self.assertEqual(Base.to_json_string(None), [])


if __name__ == '__main__':
    unittest.main()