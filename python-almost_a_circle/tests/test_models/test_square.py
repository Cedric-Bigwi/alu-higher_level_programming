#!/usr/bin/python3
"""Unittest for Square class"""
import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    def test_size_setter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual(s.size, 10)

    def test_update_args(self):
        s = Square(2)
        s.update(89, 4, 1, 2)
        self.assertEqual(str(s), "[Square] (89) 1/2 - 4")

    def test_update_kwargs(self):
        s = Square(3)
        s.update(id=99, size=7, y=2)
        self.assertEqual(str(s), "[Square] (99) 0/2 - 7")

    def test_to_dictionary(self):
        s = Square(4, 1, 2, 10)
        self.assertEqual(s.to_dictionary(), {"id": 10, "size": 4, "x": 1, "y": 2})
