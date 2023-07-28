from unittest import TestCase

from day_03_2015 import deliver_presents


class Test(TestCase):
    def test_deliver_presents(self):
        test_instructions: str = '^^>v<'
        result = deliver_presents(test_instructions)
        assert len(result) == 5
        assert result == {(0, 0): 1, (0, 1): 2, (0, 2): 1, (1, 2): 1, (1, 1): 1}
        assert result[(0, 0)] == 1
        assert result[(0, 2)] == 1
        assert result[(1, 2)] == 1
        assert result[(1, 1)] == 1
        assert result[(0, 1)] == 2
