#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_no_args(self):
        self.assertEqual(max_integer([]), None)

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_beginning_end(self):
        self.assertEqual(max_integer([5, 1, 3]), 5)

    def test_middle_end(self):
        self.assertEqual(max_integer([1, 5, 3]), 5)

    def test_negative(self):
        self.assertEqual(max_integer([-1, 5, 3]), 5)

    def test_only_negative(self):
        self.assertEqual(max_integer([-1, -5, -3]), -1)

    def test_list_one(self):
        self.assertEqual(max_integer([3]), 3)

if __name__ == '__main__':
    unittest.main()
