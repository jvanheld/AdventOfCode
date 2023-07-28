"""
Solutions for the challenges of the 2015 session of Advent Of Code.

https://adventofcode.com/2015

"""

from day_01_2015 import find_floor, first_basement
from day_02_2015 import calc_paper_and_ribbon
from day_03_2015 import deliver_presents
from util import read_string, read_list


def day01():
    """
    Find the floor for Santa Claus
    """
    floorstring = read_string('2015/data/data_2015_01.txt')
    floor = find_floor(floorstring)
    print(f"Floor for day 01: {floor}")
    basement = first_basement(floorstring)
    print(f"First time in basement: {basement}")


def day02():
    """
    Compute wrapping paper surface
    """
    dimensions = read_list('2015/data/data_2015_02.txt')
    total_surface, total_ribbon = calc_paper_and_ribbon(dimensions)
    print(f"Total wrapping paper surface: {total_surface}")
    print(f"Total ribbon length: {total_ribbon}")


def day03():
    """
    Deliver presents in an infinite array of houses
    """
    move_instructions = read_string('2015/data/data_2015_03.txt')
    # print(f"Move instructions: {move_instructions}")
    presents_per_house = deliver_presents(move_instructions)
    print(f"Number of houses with at least one present: {len(presents_per_house)}")


def main():
    print("Day 01")
    day01()

    print("\nDay 02")
    day02()

    print("\nDay 03")
    day03()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
