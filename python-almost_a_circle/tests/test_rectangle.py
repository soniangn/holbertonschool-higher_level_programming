#!/usr/bin/python3
""" Unittest for Rectangle
"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


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

    def test_rectangle_errors(self):
        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

    def test_rectangle_area(self):
        obj = Rectangle(3, 4)
        self.assertEqual(obj.area(), 12)

    def test_rectangle_str(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    def test_rectangle_display(self):
        obj = Rectangle(3, 2, 0, 0)
        self.assertEqual(obj.display(), None)
    
    def test_rectangle_to_dictionary(self):
        obj = Rectangle(3, 2, 4, 5, 1)
        self.assertEqual(obj.to_dictionary(), {'id': 1, 'width': 3, 'height': 2, 'x': 4, 'y': 5})

    def test_rectangle_update_1(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update()
        self.assertEqual(obj.id, 5)

    def test_rectangle_update_2(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(89)
        self.assertEqual(obj.id, 89)

    def test_rectangle_update_3(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(89, 1)
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)

    def test_rectangle_update_4(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(89, 1, 2)
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)

    def test_rectangle_update_5(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(89, 1, 2, 3)
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)

    def test_rectangle_update_6(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(89, 1, 2, 3, 4)
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_rectangle_update_7(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(**{ 'id': 89})
        self.assertEqual(obj.id, 89)

    def test_rectangle_update_8(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(**{ 'id': 89, 'width': 1})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)

    def test_rectangle_update_9(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(**{ 'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
    
    def test_rectangle_update_10(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)

    def test_rectangle_update_11(self):
        obj = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(obj.id, 5)
        obj.update(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(obj.id, 89)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)

    def test_rectangle_create_1(self):
        obj = Rectangle.create(**{ 'id': 89})
        self.assertEqual(obj.id, 89)

    def test_rectangle_create_2(self):
        obj = Rectangle.create(**{ 'id': 89, 'width': 1})
        self.assertEqual(obj.width, 1)

    def test_rectangle_create_3(self):
        obj = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2})
        self.assertEqual(obj.height, 2)
    
    def test_rectangle_create_4(self):
        obj = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3})
        self.assertEqual(obj.x, 3)

    def test_rectangle_create_5(self):
        obj = Rectangle.create(**{ 'id': 89, 'width': 1, 'height': 2, 'x': 3, 'y': 4})
        self.assertEqual(obj.y, 4)

    def test_rectangle_save_to_file_none(self):
        self.assertEqual(Rectangle.save_to_file(None), None)

    def test_rectangle_save_to_file_empty(self):
        self.assertEqual(Rectangle.save_to_file([]), None)

    def test_rectangle_save_to_file_rect(self):
        obj = Rectangle(1, 2)
        self.assertEqual(Rectangle.save_to_file(obj), 0)

    def test_rectangle_load_from_file_rect(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()


if __name__ == '__main__':
    unittest.main()
