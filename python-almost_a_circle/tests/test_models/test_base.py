#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id(self):
        b = Base(100)
        self.assertEqual(b.id, 100)
