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
"""


def init_matrix(nrow, ncol, fill_value=0):
    """
    Create a nrow x ncol matrix filled with the specified value.

    :param nrow: number of rows
    :param ncol: number of columns
    :param fill_value: value to instantiate each cell of the matrix
    :return: a 2D array of the specified dimensions filled in with the fill value.
    """
    return [[fill_value for j in range(ncol)] for i in range(nrow)]


def print_matrix(matrix, sep='\t'):
    """
    Print the content of a matrix
    :param matrix: matrix to print
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
    for i in list(range(top, bottom)):
        for j in list(range(left, right)):
            matrix[i][j] = value
    return matrix
