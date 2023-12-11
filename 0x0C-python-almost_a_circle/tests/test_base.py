#!/usr/bin/python3
"""Test cases for Base class"""
import unittest
from models.base import Base


class TestBaseCLass(unittest.TestCase):
    """Test cases for Base classes"""
    def test_to_json_string(self):
        base = Base()
        self.assertEqual(base.to_json_string(None), "[]")
        #Check if func actually returns a json string representation
        ret_val = base.to_json_string([])
        #Check if func actually receives params of type list

    def test_save_to_file(self):
        base = Base()
        #No 16

    def test

    def tearDown(self):
        self.base.dispose()
