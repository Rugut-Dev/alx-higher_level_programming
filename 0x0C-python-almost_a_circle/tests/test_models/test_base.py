#!/usr/bin/python3
"""Test cases for Base class"""
import unittest
from models.base import Base


class TestBaseCLass(unittest.TestCase):
    """Test cases for Base classes"""
    def test_to_json_string(self):
        base = Base()
        self.assertEqual(base.to_json_string(None), "[]")

    """tests if protected attribute"""
    def test_private_class_attr(self):
        base = Base()
        attrs = dir(base)
        self.assertIn('_Base__nb_objects', attrs)

    """Test if id is None, __nb_objects should be incremented and = id"""
    def test_constructor_with_id(self):
        base = Base(5)
        self.assertEqual(base.id, 5)

    def test_constructor_without_id(self):
        base = Base()
        base2 = Base()
        self.assertEqual(base.id, 1)
        self.assertEqual(base2.id, 2)

    """Test if this its the super class"""
    def test_super_class(self):
        self.assertTrue(issubclass(Base, object))
