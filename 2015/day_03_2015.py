"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him
via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>),
or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off,
and Santa ends up visiting some houses more than once.

How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.


--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents
with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns
moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.

"""
from tqdm import tqdm

from util import read_string

def one_move(x: int, y: int, char: str):
    """
    Update latitude (X) or longitude (Y) depending on the move character.

    :param x: starting latitude
    :param y: starting longitude
    :param move: move character. Supported: north (^), south (v), east (>), west (<)
    :return: a tuple with updated x and y coordinates
    """
    if char == "^":
        y += 1
    elif char == ">":
        x += 1
    elif char == "<":
        x -= 1
    elif char == "v":
        y -= 1
    else:
        Exception(f"Invalid character in move instructions: {char}")
    return x, y

def deliver_presents(move_instructions: str):
    """
    Compute the number of presents assigned to each house as a function of Santa's moves.

    Moves are coded as a succession of characters: north (^), south (v), east (>), west (<).

    :param move_instructions: string containing the move instructions
    :return: a dictionary with the house coordinates (tuples) as key, and the number of presents per house as values
    """
    presents_per_house = {}
    x = 0
    y = 0
    char = "."
    presents_per_house[(x, y)] = 1
    # print(f'\t{char}\t{x}\t{y}\t{presents_per_house[(x, y)]}')
    for char in tqdm(move_instructions):
        x, y = one_move(x, y, char)
        presents_per_house[(x, y)] = presents_per_house.get((x, y), 0) + 1
        # print(f'\t{char}\t{x}\t{y}\t{presents_per_house[(x, y)]}')

    return presents_per_house


def deliver_presents_with_robot(move_instructions: str):
    """
    Compute the number of presents assigned to each house as a function of the alternating moves of Santa and
    Robo-Santa.

    Moves are coded as a succession of characters: north (^), south (v), east (>), west (<).

    :param move_instructions: string containing the move instructions
    :return: a dictionary with the house coordinates (tuples) as key, and the number of presents per house as values
    """
    # print('Initializing')
    # print(f'\tMove instructions:\t{move_instructions}')

    # Initialize  parameters for Santa
    instructions_santa = move_instructions[0:(len(move_instructions)):2]
    # print(f'\tMove instructions for Santa:\t{instructions_santa}')

    x_santa = 0
    y_santa = 0

    # Initialize parameters for Robo-Santa
    instructions_robot = move_instructions[1:(len(move_instructions)):2]
    # print(f'\tMove instructions for Robo-Santa:\t{instructions_robot}')
    x_robot = 0
    y_robot = 0

    presents_per_house = {}
    char = "."
    presents_per_house[(0, 0)] = 1

    # print("\nStart point")
    # print(f'\t{char}\t{0}\t{0}\t{presents_per_house[(0, 0)]}')

    # print("\nSantas' trajectory")
    for char in tqdm(instructions_santa):
        x_santa, y_santa = one_move(x_santa, y_santa, char)
        presents_per_house[(x_santa, y_santa)] = presents_per_house.get((x_santa, y_santa), 0) + 1
        # print(f'\t{char}\t{x_santa}\t{y_santa}\t{presents_per_house[(x_santa, y_santa)]}')

    # print("\nRobo-Santa's trajectory")
    for char in tqdm(instructions_robot):
        x_robot, y_robot = one_move(x_robot, y_robot, char)
        presents_per_house[(x_robot, y_robot)] = presents_per_house.get((x_robot, y_robot), 0) + 1
        # print(f'\t{char}\t{x_robot}\t{y_robot}\t{presents_per_house[(x_robot, y_robot)]}')

    return presents_per_house


def day03():
    """
    Deliver presents in an infinite array of houses
    """
    move_instructions = read_string('2015/data/data_2015_03.txt')
    # print(f"Move instructions: {move_instructions}")

    print("\n\nDay 03 - Part One")
    presents_per_house = deliver_presents(move_instructions)
    print(f"\tNumber of houses with at least one present (Santa alone): {len(presents_per_house)}")

    print("\nDay 03 - Part Two")
    presents_per_house = deliver_presents_with_robot(move_instructions)
    print(f"\tNumber of houses with at least one present (Santa + Robo-Santa): {len(presents_per_house)}")
