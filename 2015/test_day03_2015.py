from unittest import TestCase

from day03_2015 import deliver_presents, deliver_presents_with_robot


class Test(TestCase):
    def test_deliver_presents(self):
        print("Part one - Test 1")
        self.assertEqual(5, len(deliver_presents('^^>v<')))
        print("Part one - Test 2")
        self.assertEqual(2, len(deliver_presents('^v^v^v^v^v')))
        # test_instructions: str = '^^>v<'
        # result = deliver_presents(test_instructions)
        # assert len(result) == 5
        # assert result == {(0, 0): 1, (0, 1): 2, (0, 2): 1, (1, 2): 1, (1, 1): 1}
        # assert result[(0, 0)] == 1
        # assert result[(0, 2)] == 1
        # assert result[(1, 2)] == 1
        # assert result[(1, 1)] == 1
        # assert result[(0, 1)] == 2

    def test_deliver_presents_with_robot(self):
        print("Part two - Test 1")
        self.assertEqual(3, len(deliver_presents_with_robot('^^>v<')))

        print("Part two - Test 2")
        self.assertEqual(11, len(deliver_presents_with_robot('^v^v^v^v^v')))
