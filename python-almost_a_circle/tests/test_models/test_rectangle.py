#!/usr/bin/python3
"""Unittest for Rectangle class"""
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(3, 4)
        self.assertEqual(r.area(), 12)

    def test_str(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_update_args(self):
        r = Rectangle(1, 1)
        r.update(10, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (10) 4/5 - 2/3")

    def test_update_kwargs(self):
        r = Rectangle(1, 1)
        r.update(id=10, width=2, height=3, x=4, y=5)
        self.assertEqual(str(r), "[Rectangle] (10) 4/5 - 2/3")
