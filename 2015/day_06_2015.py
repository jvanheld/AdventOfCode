"""--- Day 6: Probably a Fire Hazard ---

--- Part One ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to
deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the
ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,
999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as
coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like
0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you
in order.

For example:

- turn on 0,0 through 999,999 would turn on (or leave on) every light.
- toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning
  on the ones that were off.
- turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.

After following the instructions, how many lights are lit?

--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from
Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or
more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.

"""

import re

import numpy as np
from tqdm import tqdm
from util import read_list


def init_matrix(nrow, ncol, fill_value=0):
    """
    Create a nrow x ncol matrix filled with the specified value.

    :param nrow: number of rows
    :param ncol: number of columns
    :param fill_value: value to instantiate each cell of the matrix
    :return: a 2D array of the specified dimensions filled in with the fill value.
    """
    return [[fill_value for _ in range(ncol)] for _ in range(nrow)]


def print_matrix(matrix, sep='\t'):
    """
    Print the content of a matrix
    :param matrix: the matrix to print
    :param sep: column separator
    :return:
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i]) - 1):
            print(matrix[i][j], end=sep)
        print(matrix[i][-1])


def rectangle_set_values(matrix, left, top, right, bottom, value=1):
    """
    Set to a given value the cells of the input matrix that are included in a given rectangle.

    :param matrix: input matrix
    :param left: left coordinate of the rectangle. Must be smaller than or equal to the right.
    :param top: rectangle top. Must be smaller than or equal to the bottom.
    :param right: rectangle right
    :param bottom: rectangle bottom
    :param value: value to set
    :return: the matrix with the modified values
    """
    # print(f'\tset\t{value} from {left},{top} to {right},{bottom}')
    for i in list(range(top, bottom + 1)):
        for j in list(range(left, right + 1)):
            matrix[i][j] = value
    return matrix


def rectangle_increase_values(matrix, left, top, right, bottom, increase=1):
    """
    Increase the values of the cells of the input matrix that are included in a given rectangle.
    A negative increase value will perform a subtraction, with a minimum of 0.

    :param matrix: input matrix
    :param left: left coordinate of the rectangle. Must be smaller than or equal to the right.
    :param top: rectangle top. Must be smaller than or equal to the bottom.
    :param right: rectangle right
    :param bottom: rectangle bottom
    :param increase: increase value
    :return: the matrix with the modified values
    """
    for i in list(range(top, bottom + 1)):
        for j in list(range(left, right + 1)):
            matrix[i][j] = matrix[i][j] + increase
            if matrix[i][j] < 0:
                matrix[i][j] = 0
    return matrix


def rectangle_toggle_values(matrix, left, top, right, bottom):
    """
    Toggle values (1 <-> 0) for the cells of the input matrix included in a given rectangle.

    :param matrix: input matrix
    :param left: left coordinate of the rectangle. Must be smaller than or equal to the right.
    :param top: rectangle top. Must be smaller than or equal to the bottom.
    :param right: rectangle right
    :param bottom: rectangle bottom
    :return: the matrix with the modified values
    """
    for i in list(range(top, bottom + 1)):
        for j in list(range(left, right + 1)):
            matrix[i][j] = 1 - matrix[i][j]
    return matrix


def day06():
    # Dictionary with the values associated to "on" and "off"
    values = {'on': 1, 'off': 0}

    # Create a 1000 x 1000 matrix with 0 values
    matrix = init_matrix(1000, 1000, values['off'])
    # matrix = np.array([[0] * 1000] * 1000, dtype="int")

    # Read instruction file
    instructions = read_list('2015/data/data_2015_06.txt')
    #    print(instructions)

    # Apply the instructions
    print("\nDay 06 - Part One")
    for instruction in tqdm(instructions):
        instr = re.split('[ ,]', instruction.strip())  # [2, 3, 5, 6]
        left, top, right, bottom = [int(instr[i]) for i in (-5, -4, -2, -1)]
        if instr[0] == 'toggle':
            matrix = rectangle_toggle_values(matrix, left, top, right, bottom)
        elif instr[0] == 'turn':
            matrix = rectangle_set_values(matrix, left, top, right, bottom, values[instr[1]])
    print("\tNumber of on lights: ", sum(map(sum, matrix)))

    print("\nDay 06 - Part Two")
    matrix = init_matrix(1000, 1000, values['off'])
    increase = {'on': 1, 'off': -1}
    for instruction in tqdm(instructions):
        instr = re.split('[ ,]', instruction.strip())  # [2, 3, 5, 6]
        left, top, right, bottom = [int(instr[i]) for i in (-5, -4, -2, -1)]
        if instr[0] == 'toggle':
            matrix = rectangle_increase_values(matrix, left, top, right, bottom, 2)
        elif instr[0] == 'turn':
            matrix = rectangle_increase_values(matrix, left, top, right, bottom, increase[instr[1]])
    print("\tTotal brightness: ", sum(map(sum, matrix)))
