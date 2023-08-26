import os
from unittest import TestCase

from day13_2015 import read_happiness_units, calc_table_happiness, optimal_happiness


class Test(TestCase):
    def test_read_hapiness_values(self):
        print(os.getcwd())
        hu = read_happiness_units(infile="data/data_2015_day13_test.txt")
        print(hu)
        # Check that the test data contains happiness units for 4 persons
        self.assertEqual(4, len(hu))

        # Test that for each of these 4 persons, the happiness units are defined for 3 persons
        for person in hu:
            self.assertEqual(3, len(hu[person]))

    def test_calc_table_happiness(self):
        hu = read_happiness_units(infile="data/data_2015_day13_test.txt")
        self.assertEqual(330, calc_table_happiness(hu, ['David', 'Alice', 'Bob', 'Carol']))

    def test_optimal_happiness(self):
        hu = read_happiness_units(infile="data/data_2015_day13_test.txt")
        best_order, best_score = optimal_happiness(hu)
        self.assertEqual(330, best_score)
#        self.assertEqual(['David', 'Alice', 'Bob', 'Carol'], best_order)
