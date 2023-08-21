#!/usr/bin/python3

"""
tests the rectangle codes
"""


import io
import unittest
import sys
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_get_width(self):
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.width, 10)

    def test_set_width(self):
        r = Rectangle(10, 20, 30, 40)
        r.width = 5
        self.assertEqual(r.width, 5)

    def test_set_width_invalid_type(self):
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(TypeError):
            r.width = "not an int"

    def test_set_width_invalid_value(self):
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(ValueError):
            r.width = -5

    def test_get_height(self):
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.height, 20)

    def test_set_height(self):
        r = Rectangle(10, 20, 30, 40)
        r.height = 5
        self.assertEqual(r.height, 5)

    def test_set_height_invalid_type(self):
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(TypeError):
            r.height = "not an int"

    def test_set_height_invalid_value(self):
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(ValueError):
            r.height = -5

    def test_get_x(self):
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.x, 30)

    def test_set_x(self):
        r = Rectangle(10, 20, 30, 40)
        r.x = 5
        self.assertEqual(r.x, 5)

    def test_set_x_invalid_type(self):
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(TypeError):
            r.x = "not an int"

    def test_set_x_invalid_value(self):
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(ValueError):
            r.x = -5

    def test_get_y(self):
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.y, 40)

    def test_set_y(self):
        r = Rectangle(10, 20, 30, 40)
        r.y = 5
        self.assertEqual(r.y, 5)

    def test_set_y_invalid_type(self):
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(TypeError):
            r.y = "not an int"

    def test_set_y_invalid_value(self):
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(ValueError):
            r.y = -5

    def test_area(self):
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(r.area(), 200)

    def test_display(self):
        r = Rectangle(2, 3, 1, 1)
        captured_output = io.StringIO()
        sys.stdout = captured_output
        r.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), "\n ##\n ##\n ##\n")

    def test_update(self):
        r = Rectangle(10, 20, 30, 40)
        r.update(1, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (1) 4/5 - 2/3")

    def test_update_invalid_args(self):
        r = Rectangle(10, 20, 30, 40)
        with self.assertRaises(TypeError):
            r.update("not an int", "not an int", "not an int", "not an int", "not an int")

    def test_str(self):
        r = Rectangle(10, 20, 30, 40)
        self.assertEqual(str(r), "[Rectangle] (None) 30/40 - 10/20")

if __name__ == '__main__':
    unittest.main()
