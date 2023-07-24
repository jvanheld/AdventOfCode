from util import read_string
from day_2015_01 import find_floor, first_basement


def day01():
    """
    Find the floor for Santa Claus
    """
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
