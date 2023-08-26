from unittest import TestCase

from day10_2015 import encode_number


class Test(TestCase):
    def test_encode_number(self):
        self.assertEqual("11", encode_number("1"))
        self.assertEqual("21", encode_number("11"))
        self.assertEqual("1211", encode_number("21"))
        self.assertEqual("111221", encode_number("1211"))
        self.assertEqual("312211", encode_number("111221"))
