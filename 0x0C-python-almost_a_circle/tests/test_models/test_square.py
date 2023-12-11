#!/usr/bin/python3
"""Test case for Square class"""


import unittest
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base
import sys
from io import StringIO


class TestSquare(unittest.TestCase):
    """Tests all cases so as to meet requirments"""
    def setUp(self):
        self.output = StringIO()
        sys.stdout = self.output
        Base._Base__nb_objects = 0

    def test_is_subclass_Rectangle(self):
        """Checks if square is child class of Rectangle"""
        self.assertTrue(issubclass(Square, Rectangle))

    def test_square_inherits(self):
        """Tests square attrs assigning"""
        sq = Square(5)
        self.assertIsInstance(sq, Square)
        self.assertIsInstance(sq, Rectangle)
        self.assertEqual(sq.width, 5)
        self.assertEqual(sq.height, 5)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)

    def test_inherited_heavviour(self):
        """Tests if square inherits Rect behaviour"""
        with self.assertRaises(ValueError):
            sq = Square(-5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq = Square("abcd")
        sq = Square(10)
        sq.x = 5
        self.assertEqual(sq.x, 5)

    def test_str_override(self):
        """Checks str output"""
        sq = Square(3, 1, 3)
        ret_val = str(sq)

        expected_output = "[Square] (1) 1/3 - 3"
        self.assertEqual(expected_output, ret_val)

    def test_area(self):
        """Tests area"""
        sq = Square(5)
        self.assertEqual(sq.area(), 25)

    def test_display(self):
        """Tests if display outputs expected output"""
        sq = Square(3, 2, 2)
        sq.display()

        expected_output = "###\n  ###\n  ###"
        printed_output = self.output.getvalue().strip()
        self.assertEqual(printed_output, expected_output)

    def test_display_without_xy(self):
        """Tests if display works"""
        sq = Square(3)
        sq.display()

        expected_output = "###\n###\n###"
        printed_output = self.output.getvalue().strip()
        self.assertEqual(printed_output, expected_output)

    def test_id_increment(self):
        """Checks if id attr is incremented when not explicitly provided"""
        sq = Square(5)
        self.assertEqual(sq.id, 1)

        sq1 = Square(3, 3)
        self.assertEqual(sq1.id, 2)

        sqb = Square(3, 1, 3, 400)
        self.assertEqual(sqb.id, 400)

    def test_size_getter(self):
        """Checks if getter works as expected"""
        sq = Square(5)
        self.assertEqual(sq.size, 5)
        sq.size = 7
        self.assertEqual(sq.size, 7)

    def test_size_setter(self):
        """Tests the setter method"""
        sq = Square(5)
        sq.size = 10
        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)

    def test_update(self):
        """Tests update method with args and kwargs"""
        sq = Square(5)
        sq.update(10)
        print(sq)
        self.assertEqual(self.output.getvalue().strip(),
                         '[Square] (10) 0/0 - 5')

    def tearDown(self):
        sys.stdout = sys.__stdout__
