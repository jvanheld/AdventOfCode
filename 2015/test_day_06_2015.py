from unittest import TestCase

from day_06_2015 import init_matrix, print_matrix, rectangle_set_values, rectangle_toggle_values


class Test(TestCase):
    def test_init_matrix(self):
        matrix = init_matrix(2, 3, 0)
        print('\ntest_init_matrix')
        print_matrix(matrix, sep='')
        self.assertEqual([[0, 0, 0], [0, 0, 0]], matrix)

    def test_rectangle_set_values(self):
        matrix = init_matrix(4, 4, 0)
        matrix = rectangle_set_values(matrix, 1, 0, 2, 1, 1)
        print('\ntest_rectangle_set_values')
        print_matrix(matrix, sep='')
        self.assertEqual([[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]], matrix)

    def test_rectangle_toggle_values(self):
        m = init_matrix(3, 3, 0)
        m = rectangle_set_values(m, 1, 1, 1, 1, 1)
        m = rectangle_toggle_values(m, 0, 0, 2, 2)
        print('\ntest_rectangle_toggle_values')
        print_matrix(m, sep='')
        self.assertEqual(8, sum(map(sum, m)))
