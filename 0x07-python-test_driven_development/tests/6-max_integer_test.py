#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class Test_Max_integer(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
    def  
