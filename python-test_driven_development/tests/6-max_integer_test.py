#!/usr/bin/python3
"""Unittest for max_integer function"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-5, -1, -8]), -1)
