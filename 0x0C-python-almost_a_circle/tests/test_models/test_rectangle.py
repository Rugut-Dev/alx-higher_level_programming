#!/usr/bin/python3
"""Test case for rectangl.py module"""
from models.rectangle import Rectangle
from models.base import Base
import unittest
import sys
from io import StringIO


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output
        Base._Base__nb_objects = 0
    """Test if Rectangle inherits from Base"""
    def test_inherits_Base(self):
        self.assertTrue(issubclass(Rectangle, Base))

    """Test for private atributes"""
    def test_width_attr(self):
        rect = Rectangle(5, 10)
        self.assertFalse(hasattr(rect, '__width'))

        self.assertTrue(hasattr(rect, 'width'))
        self.assertEqual(rect.width, 5)

        rect.width = 66
        self.assertEqual(rect.width, 66)

    def test_height_attr(self):
        rect = Rectangle(5, 10)
        self.assertFalse(hasattr(rect, '__height'))

        self.assertTrue(hasattr(rect, 'height'))
        self.assertEqual(rect.height, 10)

        rect.height = 66
        self.assertEqual(rect.height, 66)

    def test_x_y_attr(self):
        rect = Rectangle(5, 10, 15, 20)
        self.assertFalse(hasattr(rect, '__x'))
        self.assertFalse(hasattr(rect, '__y'))

        self.assertTrue(hasattr(rect, 'x'))
        self.assertTrue(hasattr(rect, 'y'))

        self.assertEqual(rect.x, 15)
        self.assertEqual(rect.y, 20)

        rect.x = 10
        rect.y = 30

        self.assertEqual(rect.x, 10)
        self.assertEqual(rect.y, 30)

    """Test if BASE logic is being applied to id"""
    def test_Base_logic_id(self):
        rect = Rectangle(10, 2)
        rect2 = Rectangle(2, 10)
        rectb = Rectangle(5, 10, 0, 0, 100)

        self.assertEqual(rect.id, 1)
        self.assertEqual(rect2.id, 2)
        self.assertEqual(rectb.id, 100)

    """Checks the EXception raised as attribuites are validated"""
    def test_exceptions(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect = Rectangle('w', 10)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect = Rectangle(7, "10")

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect = Rectangle(5, 10, 'x', 8)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect = Rectangle(5, 10, 8, 'y')

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect = Rectangle(-5, 10)

        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect = Rectangle(5, -4)

        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect = Rectangle(5, 10, -4, 7)

        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect = Rectangle(5, 10, 5, -2)

    """Lets test if area is calculated correctly"""
    def test_area(self):
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    """Test case for correct output"""
    def test_display(self):
        rect = Rectangle(4, 2)
        rect.display()

        printed_output = self.output.getvalue().strip()
        expected_output = "####\n####"

        self.assertEqual(printed_output, expected_output)

    def test_str_override(self):
        """Test the __str__ method"""
        rect = Rectangle(5, 5, 1)
        ret_val = str(rect)

        expected_output = "[Rectangle] (1) 1/0 - 5/5"
        self.assertEqual(ret_val, expected_output)

    def tearDown(self):
        sys.stdout = sys.__stdout__
