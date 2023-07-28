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



"""


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
    # print(f'\t{char}\t{x}\t{y}\t{presents_per_house[(x, y)]}\n')
    for char in move_instructions:
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

        presents_per_house[(x, y)] = presents_per_house.get((x, y), 0) + 1
        # print(f'\t{char}\t{x}\t{y}\t{presents_per_house[(x, y)]}\n')

    return presents_per_house
