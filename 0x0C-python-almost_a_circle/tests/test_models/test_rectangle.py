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

    def test_display_xy(self):
        """Tests the output as per the args"""
        rect =  Rectangle(2, 3, 2, 2)
        rect.display()

        expected_output = "##\n  ##\n  ##"
        printed_output = self.output.getvalue().strip()
        self.assertEqual(printed_output, expected_output)

    def test_update_method(self):
        """Test if update method assigns arguments correctly"""
        rect = Rectangle(1, 1, 1, 1, 1)
        rect.update(5, 10, 15, 20, 25)
        self.assertEqual(rect.id, 5)
        self.assertEqual(rect.width, 10)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 20)
        self.assertEqual(rect.y, 25)

        rect.update(7, 12)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 12)
        self.assertEqual(rect.height, 15)
        self.assertEqual(rect.x, 20)
        self.assertEqual(rect.y, 25)

    def test_update_with_args_kwargs9(self):
        rect = Rectangle(10, 10, 10, 10)
        expected_output = "[Rectangle] (1) 10/10 - 10/10"

        self.assertEqual(str(rect), expected_output)

        rect.update(height=1)
        expected_output = "[Rectangle] (1) 10/10 - 10/1"
        self.assertEqual(str(rect), expected_output)

        rect.update(width=1, x=2)
        expected_output = "[Rectangle] (1) 2/10 - 1/1"
        self.assertEqual(str(rect), expected_output)

        rect.update(y=1, width=2, x=3, id=89)
        expected_output = "[Rectangle] (89) 3/1 - 2/1"
        self.assertEqual(str(rect), expected_output)

        rect.update(x=1, height=2, y=3, width=4)
        expected_output = "[Rectangle] (89) 1/3 - 4/2"
        self.assertEqual(str(rect), expected_output)

    def test_to_dictionary(self):
        """Tests json.loads"""
        rect = Rectangle(5, 10, 2, 4, 1)
        expected_output = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 4}
        self.assertEqual(rect.to_dictionary(), expected_output)

    def tearDown(self):
        sys.stdout = sys.__stdout__
