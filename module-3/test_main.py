"""
Small test suite for add and subtract() methods
"""

import unittest

from main import add, subtract


class TestMain(unittest.TestCase):

    def test_add(self):
        actual = add(3, 3)
        expected = 6
        assert actual == expected

    def test_subtract(self):
        actual = subtract(100, 20)
        expected = 30
        assert actual == expected