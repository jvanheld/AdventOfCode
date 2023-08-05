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


def main():
    cProfile.run('day01()')
    cProfile.run('day02()')
    cProfile.run('day03()')
    # cProfile.run('day04()')
    cProfile.run('day05()')
    cProfile.run('day06()')
    print("\n\nAll days done\n\n")


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
