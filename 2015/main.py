"""
Solutions for the challenges of the 2015 session of Advent Of Code.

https://adventofcode.com/2015

"""

import cProfile
from day_01_2015 import day01
from day_02_2015 import day02
from day_03_2015 import day03
from day_04_2015 import day04
from day_05_2015 import day05
from day_06_2015 import day06
from day_07_2015 import day07
from day_08_2015 import day08
from day_09_2015 import day09
from day_10_2015 import day10


def main():
    all_days = False
    if all_days: day01()
    if all_days: day02()
    if all_days: day03()
    if all_days: day04()
    if all_days: day05()
    if all_days: day06()
    if all_days: day07()
    if all_days: day08()
    if all_days: day09()
    day10()


print("\n\nAll days done\n\n")

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
