from unittest import TestCase
from day_08_2015 import decode, encode


class Test(TestCase):
    def test_decode(self):
        self.assertEqual(0, len(decode('""')))
        self.assertEqual(3, len(decode('"abc"')))
        self.assertEqual(7, len(decode('"aaa\\"aaa"')))
        self.assertEqual(1, len(decode('"\\x39"')))

    def test_encode(self):
        self.assertEqual(6, len(encode('""')))
        self.assertEqual(9, len(encode('"abc"')))
        self.assertEqual(16, len(encode('"aaa\\"aaa"')))
        self.assertEqual(11, len(encode('"\\x27"')))
