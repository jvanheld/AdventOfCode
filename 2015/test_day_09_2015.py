from unittest import TestCase

from day_09_2015 import permutations


class Test(TestCase):
    def test_permutations(self):
        self.assertEqual([], permutations([]))
        self.assertEqual([["Bruxelles"]], permutations(["Bruxelles"]))
        self.assertEqual([['a', 'b'], ['b', 'a']], permutations(['a', 'b']))
