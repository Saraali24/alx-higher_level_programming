#!/usr/bin/python3
"""TestClass
"""
import unittest
max_integer = __import__('6-max_integer').max_integer
class TestClass(unittest.TestCase):
    """ TestClass"""
    def test_one(self):
        """test_one""" 
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)  
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)
        self.assertEqual(max_integer([1, 10, 2]), 10)
        self.assertEqual(max_integer([-1, 10, 2]), 10)
        self.assertEqual(max_integer([-5]), -5)
        self.assertEqual(max_integer([20]), 20)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
