from unittest import TestCase

from day_05_2015 import check_rules


class Test(TestCase):
    def test_check_rules(self):
        self.assertTrue(check_rules('ugknbfddgicrmopn'))
        self.assertFalse(check_rules('jchzalrnumimnmhp'))
        self.assertFalse(check_rules('dvszwmarrgswjxmb'))
