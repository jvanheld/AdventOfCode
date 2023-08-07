from unittest import TestCase

from bitstring import BitArray

from day_07_2015 import shift_bits


class Test(TestCase):
    def test_shift_bits(self):
        self.assertEqual('0100', shift_bits(BitArray(uint=8, length=4), shift=1, length=4).bin)
        self.assertEqual('10000', shift_bits(BitArray(uint=8, length=5), shift=-1, length=5).bin)
