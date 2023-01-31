#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_no_args(self):
        self.assertEqual(max_integer([]), None)

class TestMaxInteger(unittest.TestCase):
    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

class TestMaxInteger(unittest.TestCase):
    def test_beginning_end(self):
        self.assertEqual(max_integer([5, 1, 3]), 5)

class TestMaxInteger(unittest.TestCase):
    def test_middle_end(self):
        self.assertEqual(max_integer([1, 5, 3]), 5)

if __name__ == '__main__':
    unittest.main()
