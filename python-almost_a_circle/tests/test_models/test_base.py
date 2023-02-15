#!/usr/bin/python3
""" Unittest for Base
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_no_args(self):
        obj = Base()
        self.assertEqual(obj.id, 1)
    
    def test_no_args_bis(self):
        obj = Base()
        self.assertEqual(obj.id, 2)

    def test_id(self):
        obj = Base(89)
        self.assertEqual(obj.id, 89)

    def test_to_json_none(self):
        obj = Base.to_json_string(None)
        self.assertEqual(obj, [])

    def test_to_json_empty_list(self):
        obj = Base.to_json_string([])
        self.assertEqual(obj, '[]')

    def test_from_json_none(self):
        obj = Base.from_json_string(None)
        self.assertEqual(obj, [])

    def test_from_json_empty(self):
        obj = Base.from_json_string("[]")
        self.assertEqual(obj, [])

    def test_from_json_none(self):
        obj = Base.from_json_string('[{ "id": 89 }]')
        self.assertEqual(obj, [{'id': 89}])


if __name__ == '__main__':
    unittest.main()
