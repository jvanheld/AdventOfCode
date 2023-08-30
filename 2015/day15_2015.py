"""
--- Day 15: Science for Hungry People ---

Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right
balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you
could use to finish the recipe (your puzzle input) and their properties per teaspoon:

- capacity (how well it helps the cookie absorb milk)
- durability (how well it keeps the cookie intact when full of milk)
- flavor (how tasty it makes the cookie)
- texture (how it improves the feel of the cookie)
- calories (how many calories it adds to the cookie)

You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can
reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (
negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3

Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each
ingredient must add up to 100) would result in a cookie with the following properties:

- A capacity of 44*-1 + 56*2 = 68
- A durability of 44*-2 + 56*3 = 80
- A flavor of 44*6 + 56*-2 = 152
- A texture of 44*3 + 56*-1 = 76

Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total
score of 62842880, which happens to be the best score possible given these ingredients. If any properties had
produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you
can make?

Your puzzle answer was 13882464.


--- Part Two ---

Your cookie recipe becomes wildly popular! Someone asks if you can make another recipe that has exactly 500 calories
per cookie (so they can use it as a meal replacement). Keep the rest of your award-winning process the same (100
teaspoons, same ingredients, same scoring system).

For example, given the ingredients above, if you had instead selected 40 teaspoons of butterscotch and 60 teaspoons
of cinnamon (which still adds to 100), the total calorie count would be 40*8 + 60*3 = 500. The total score would go
down, though: only 57600000, the best you can do in such trying circumstances.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you
can make with a calorie total of 500?


"""
import os

import numpy as np
from tqdm import tqdm

from util import read_list


def read_data(infile: str):
    """
    Parse input file to extract the features of food ingredients.

    :param infile: path of the input file
    :return: a dictionary with ingredients as keys, and dictionaries of features as values
    """
    values = dict()
    ingredients = list()
    features = list()
    calories = list()
    instructions = read_list(infile)
    nb_features = 4
    nb_ingredients = len(instructions)
    values = np.array([[0 for _ in range(nb_features)] for _ in range(nb_ingredients)])
    for i, instr in enumerate(instructions):
        # Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
        ingredient, feature_values = instr.strip().split(sep=": ")
        ingredients.append(ingredient)
        fields = feature_values.split(sep=", ")
        for j, field in enumerate(fields):
            key, value = field.split(sep=' ')
            # print(f"{ingredient}\t{j}\t{key}\t{value}")
            if i == 0:
                features.append(key)

            if key == "calories":
                calories.append(int(value))
            else:
                values[i][j] = int(value)
    # print(f"Ingredients:\t{ingredients}")
    # print(f"feature_names\t{features}")
    # print("food_features\n", food_features)
    return ingredients, calories, features, values


def all_partitions(n=100, groups=4):
    partitions = list()
    # print(f"all_partitions({n}, {groups})")
    if groups == 1:
        partitions = [[n]]
        # print(f"One group\tt{type(partitions)}\t{partitions}")
    else:
        for i in range(0, n + 1):
            # print(f"{n}\t{groups}\t{i}")
            sub_partitions = all_partitions(n - i, groups - 1)
            for partition in sub_partitions:
                # print(f"concat\t{i}\t{partition}")
                partitions.append([i] + partition)
    return partitions


def food_value(percentages, values):
    sum_per_feature = percentages[0] * values[0]
    # print(f"{percentages[0]}\t{values[0]}\t{sum_per_feature}")
    for i in range(1, len(percentages)):
        sum_per_feature += percentages[i] * values[i]
        # print(f"{percentages[i]}\t{values[i]}\t{sum_per_feature}")
    sum_per_feature = np.maximum(sum_per_feature, [0] * len(sum_per_feature))
    return np.prod(sum_per_feature)


def day15():
    ingredients, calories, features, values = read_data('2015/data/data_2015_day15.txt')
    # print(f"\tvalues\t{values}")
    # print(f"\tcalories\t{calories}")
    best_value = 0
    best_value_500cal = 0
    n_500cal = 0  # number of percentages with exactly 500 calories
    # values_no_cal = values[0:len(ingredients), 0:4]  # Values without the calories
    # print(values_no_cal)

    for percentages in tqdm(all_partitions(n=100, groups=len(ingredients))):

        # print(percentages)
        current_value = food_value(percentages, values)
        if current_value > best_value:
            best_value = current_value
            best_percentages = percentages

        cal = np.matmul(percentages, calories)
        if cal == 500:
            n_500cal += 1
            # print(f"\tpercentages: {percentages}\tcalories: {calories}\t{cal}")
            if current_value > best_value_500cal:
                best_value_500cal = current_value
                best_percentages_500cal = percentages

    print(f"\n\nDay 15 - Part One")
    print(f"\tBest value: {best_value}")
    print(f"\tBest percentages: {best_percentages}")

    print(f"\n\nDay 15 - Part Two")
    print(f"\tNumber of recipes with 500 cal: {n_500cal}")
    print(f"\tBest value for 500 cal: {best_value_500cal}")
    print(f"\tBest percentages for 500 cal: {best_percentages_500cal}")


if __name__ == '__main__':
    os.chdir('..')
    day15()
