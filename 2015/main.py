"""
Solutions for the challenges of the 2015 session of Advent Of Code.

https://adventofcode.com/2015

"""

from day_01_2015 import find_floor, first_basement
from util import read_string


def day01():
    """
    Find the floor for Santa Claus
    """
    print("Day 01 challenge")
    floorstring = read_string('2015/data/2015_01.txt')
    floor = find_floor(floorstring)
    print(f"Floor for day 01: {floor}")
    basement = first_basement(floorstring)
    print(f"First time in basement: {basement}")


def main():
    day01()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
