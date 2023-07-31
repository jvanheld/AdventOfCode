"""
Solutions for the challenges of the 2015 session of Advent Of Code.

https://adventofcode.com/2015

"""

from day_01_2015 import find_floor, first_basement
from day_02_2015 import calc_paper_and_ribbon
from day_03_2015 import deliver_presents, deliver_presents_with_robot
from day_04_2015 import find_suffix_number
from util import read_string, read_list


def day01():
    """
    Find the floor for Santa Claus
    """
    floorstring = read_string('2015/data/data_2015_01.txt')
    floor = find_floor(floorstring)
    print("\nDay 01 - Part One")
    print(f"\tFloor: {floor}")
    basement = first_basement(floorstring)
    print("Day 01 - Part Two")
    print(f"\tFirst time in basement: {basement}")


def day02():
    """
    Compute wrapping paper surface
    """
    dimensions = read_list('2015/data/data_2015_02.txt')
    total_surface, total_ribbon = calc_paper_and_ribbon(dimensions)
    print("\nDay 02 - Part One")
    print(f"\tTotal wrapping paper surface: {total_surface}")
    print("Day 02 - Part Two")
    print(f"\tTotal ribbon length: {total_ribbon}")


def day03():
    """
    Deliver presents in an infinite array of houses
    """
    move_instructions = read_string('2015/data/data_2015_03.txt')
    # print(f"Move instructions: {move_instructions}")

    print("\nDay 03 - Part One")
    presents_per_house = deliver_presents(move_instructions)
    print(f"\tNumber of houses with at least one present (Santa alone): {len(presents_per_house)}")

    print("Day 03 - Part Two")
    presents_per_house = deliver_presents_with_robot(move_instructions)
    print(f"\tNumber of houses with at least one present (Santa + Robo-Santa): {len(presents_per_house)}")


def day04():
    puzzle_input = 'iwrupvqb'
    print("Day 04 - Part One")
    print('\t', find_suffix_number(puzzle_input, 5))
    print("Day 04 - Part Two")
    print('\t', find_suffix_number(puzzle_input, 6))


def main():
    day01()
    day02()
    day03()
    day04()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
