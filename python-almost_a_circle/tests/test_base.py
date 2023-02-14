#!/usr/bin/python3
""" Unittest for Base
"""
from models.base import Base

class TestBase(unittest.TestCase):
    def test_bla(self):
        self.assertEqual(Base(), 1)



if __name__ == '__main__':
    unittest.main()