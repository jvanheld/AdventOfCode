from unittest import TestCase

from day_05_2015 import check_rules_part_one, check_rules_part_two


class Test(TestCase):
    def test_check_rules_part_one(self):
        # ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...),
        # and none of the disallowed substrings.
        self.assertTrue(check_rules_part_one('ugknbfddgicrmopn'))

        # aaa is nice because it has at least three vowels and a double letter, even though the letters used by
        # different rules overlap.
        self.assertTrue(check_rules_part_one('aaa'))

        # jchzalrnumimnmhp is naughty because it has no double letter.
        self.assertFalse(check_rules_part_one('jchzalrnumimnmhp'))

        # haegwjzuvuyypxyu is naughty because it contains the string xy.
        self.assertFalse(check_rules_part_one('haegwjzuvuyypxyu'))

        # dvszwmarrgswjxmb is naughty because it contains only one vowel.
        self.assertFalse(check_rules_part_one('dvszwmarrgswjxmb'))

    def test_check_rules_part_one(self):
        # qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly
        # one letter between them (zxz).
        self.assertTrue(check_rules_part_two('qjhvhtzxzqqjkmpb'))

        # xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though
        # the letters used by each rule overlap.
        self.assertTrue(check_rules_part_two('xxyxx'))

        # uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
        self.assertFalse(check_rules_part_two('uurcxstgmygtbstg'))

        # ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that
        # appears twice.
        self.assertFalse(check_rules_part_two('ieodomkazucvgmuy'))
