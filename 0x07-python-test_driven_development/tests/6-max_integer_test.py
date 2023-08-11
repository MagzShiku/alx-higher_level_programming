#!/usr/bin/python3

"""
    write unittests for the function def max_integer(list=[]):
"""


import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
    """
        write unittests for the function def max_integer(list=[]):
    """
    self.assertEqual(max_integer([1, 2, 3, 4]), 4)
    self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
    self.assertEqual(max_integer([0]), 0)
    self.assertEqual(max_integer([0]), 0)
    self.assertEqual(max_integer([1]), 1)
