from unittest import TestCase

from day_05_2015 import check_vowels


class Test(TestCase):
    def test_check_rules(self):
        self.assertTrue(check_vowels('aueeiiioooouuuuu'))
        self.assertTrue(check_vowels('ugknbfddgicrmopn'))
        self.assertFalse(check_vowels('jchzalrnumimnmhp'))
