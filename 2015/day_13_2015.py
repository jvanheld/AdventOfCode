"""
--- Day 13: Knights of the Dinner Table ---

In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year,
you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward
conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they
were to find themselves sitting next to each other person. You have a circular table that will be just big enough to
fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.

Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much),
but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally,
seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The
arrangement looks like this:

     +41 +46
+55   David    -2
Carol       Alice
+60    Bob    +54
     -7  +83

After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most
optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?

--- Part Two ---

In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the
whole thing, and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone
else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?



"""

import os
from itertools import permutations

from tqdm import tqdm

from util import read_list


def read_happiness_units(infile: str):
    """
    Parse a text file defining the hapiness units between each pair of guests.

    :param infile: input file :return: a dictionary of dictionaries, where the keys inidcate the guests,
    and the values the hapiness units from the first key to the second key.

    """
    instructions = read_list(infile)
    happiness_dict = dict()
    sign = {"gain": +1, "lose": -1}
    for instr in instructions:
        items = instr.strip().strip('.').split(sep=" ")
        if not items[0] in happiness_dict:
            happiness_dict[items[0]] = dict()
        happiness_dict[items[0]][items[10]] = sign[items[2]] * int(items[3])
        # print(items)
    return happiness_dict


def calc_table_happiness(happiness_dict: dict, guest_order: list):
    """
    Compute the happiness score of a table given the order of the guests.

    :param guest_order: a list with the order of the guests
    :return: happiness score of the
    """
    # print(happiness_dict)

    # Init with the score from the last to the first guest
    # happiness_score = happiness_dict[guest_order[-1]][guest_order[0]] + happiness_dict[guest_order[0]][guest_order[-1]]
    happiness_score = 0

    # Add scores for successive pairs from the first to the last guest
    for guest1, guest2 in zip(guest_order, guest_order[1:] + [guest_order[0]]):
        # print(f"Guest 1: {guest1}\tGuest 2: {guest2}\tunits: {happiness_dict[guest1]}")
        happiness_score += happiness_dict[guest1][guest2] + happiness_dict[guest2][guest1]
    # print(f"Happiness score: {happiness_score}")
    return happiness_score


def optimal_happiness(happiness_dict: dict):
    """
    Find the optimal guest order by computing the score of all possible guest permutations.

    :param happiness_dict: dictionary with the hapiness units for each pair of guests
    :return: a list with the optimal order of guests, and the score of the corresponding table
    """
    guests = happiness_dict.keys()
    best_score = 0
    for perm in tqdm(permutations(guests)):
        guest_oder = list(perm)
        score = calc_table_happiness(happiness_dict, guest_oder)
        if score > best_score:
            best_score = score
            best_order = guest_oder
        # print(f"{perm}\t{score}")
    return best_order, best_score


def day13():
    hu = read_happiness_units(infile="2015/data/data_2015_13.txt")
    best_order, best_score = optimal_happiness(hu)

    print(f"\n\nDay 13 - Part One")
    print(f"Best score: {best_score}\tbest order: {best_order}")

    print(f"\nDay 13 - Part Two")
    best_score_with_me = 0
    for guest1, guest2 in zip(best_order, best_order[1:] + [best_order[0]]):
        score_with_me = best_score - hu[guest1][guest2] - hu[guest2][guest1]
        if best_score_with_me < score_with_me:
            best_score_with_me = score_with_me
    print(f"Best score with me: {best_score_with_me}")

if __name__ == '__main__':
    os.chdir('..')
    day13()
