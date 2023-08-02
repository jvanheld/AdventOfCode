from unittest import TestCase

from day_05_2015 import check_rules


class Test(TestCase):
    def test_check_rules(self):
        # ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...),
        # and none of the disallowed substrings.
        self.assertTrue(check_rules('ugknbfddgicrmopn'))

        # aaa is nice because it has at least three vowels and a double letter, even though the letters used by
        # different rules overlap.
        self.assertTrue(check_rules('aaa'))

        # jchzalrnumimnmhp is naughty because it has no double letter.
        self.assertFalse(check_rules('jchzalrnumimnmhp'))

        # haegwjzuvuyypxyu is naughty because it contains the string xy.
        self.assertFalse(check_rules('haegwjzuvuyypxyu'))

        # dvszwmarrgswjxmb is naughty because it contains only one vowel.
        self.assertFalse(check_rules('dvszwmarrgswjxmb'))
