from unittest import TestCase

from day_04_2015 import find_suffix_number


class Test(TestCase):
    def test_find_suffix_number(self):
        self.assertEqual(('abcdef', 609043, 'abcdef609043', '000001dbbfa3a5c83a2d506429c7b00e'),
                         find_suffix_number('abcdef', 5))
        self.assertEqual(('pqrstuv', 1048970, 'pqrstuv1048970', '000006136ef2ff3b291c85725f17325c'),
                         find_suffix_number('pqrstuv', 5))
