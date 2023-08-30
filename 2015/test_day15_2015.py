from unittest import TestCase

import numpy as np

from day15_2015 import food_value, all_partitions, read_data


class Test(TestCase):
    def test_data(self):
        ingredients = ["Butterscotch", "Cinnamon"]
        features = ["capacity", "durability", "flavor", "texture", "calories"]
        values = np.array([[-1, -2, 6, 3, 8],
                           [2, 3, -2, -1, 3]])
        return ingredients, features, values

    def test_calc_value(self):
        """
        Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
        Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

        Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each
        ingredient must add up to 100) would result in a cookie with the following properties:

        - A capacity of 44*-1 + 56*2 = 68
        - A durability of 44*-2 + 56*3 = 80
        - A flavor of 44*6 + 56*-2 = 152
        - A texture of 44*3 + 56*-1 = 76

        Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total
        score of 62842880, which happens to be the best score possible given these ingredients. If any properties had
        produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

        """
        incredients, features, values = self.test_data()
        self.assertEqual(62842880, food_value([44, 56], values[0:2, 0:4]))

    def test_all_partitions(self):
        self.assertEqual([[5]], all_partitions(n=5, groups=1))
        self.assertEqual([[0, 3], [1, 2], [2, 1], [3, 0]], all_partitions(n=3, groups=2))
        self.assertEqual([[0, 0, 2], [0, 1, 1], [0, 2, 0], [1, 0, 1], [1, 1, 0], [2, 0, 0]],
                         all_partitions(n=2, groups=3))

    def test_quick_test(self):
        ingredients, calories, features, values = read_data('data/data_2015_day15.txt')
        percentages = [28, 32, 18, 22]
        print(food_value(percentages, values))
