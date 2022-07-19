#!usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_passing(self):
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([2, 4, 20]), 20)
        self.assertEqual(max_integer([1000, 10000, 500000]), 500000)
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([-1000000, 1, 2, 3]), 3)
        self.assertEqual(max_integer([-1000000, 10000, 2.5, 3, 10000000000]),
                         10000000000)

    def test_failing(self):
        self.assertRaises(TypeError, max_integer, 1)
        self.assertRaises(TypeError, max_integer, 1.3)
        self.assertRaises(TypeError, max_integer, -3)
        self.assertRaises(TypeError, max_integer, 2j)
        self.assertRaises(TypeError, max_integer, [2j, 3])
        self.assertRaises(TypeError, max_integer, [-2, "90"])
