"""
--- Day 9: All in a Single Night ---

--- Part One ---

Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair
of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly
once. What is the shortest distance he can travel to achieve this?


For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982

The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?

--- Part Two ---

The next year, just to show off, Santa decides to take the route with the longest distance instead.

He can still start and end at any two (different) locations he wants, and he still must visit each location exactly
once.

For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.

What is the distance of the longest route?
"""
import itertools
from math import factorial
from time import time

from tqdm import tqdm

from util import read_list


def read_distances(infile: str):
    """
    Parse the input file to instantiate the list (set) of cities and the distance matrix.

    :param infile: a text file with one distance per row
    :return: a set with the names of cities and a matrix with the distances between cities
    """
    lines = read_list(infile)
    distances = dict()
    cities = set()
    for line in lines:
        line = line.strip()
        # print(line)
        # Norrath to Tambi = 82
        start, end, dist = line.split(sep=" ")[0:5:2]
        distances[start, end] = int(dist)
        distances[end, start] = int(dist)
        cities.add(start)
        cities.add(end)
    return cities, distances


def permutations(lst: list):
    """
    Compute the list of all permutations for the input set (list).
    Note: inefficient recursive implementation, replaced by a call to itertools.permutations() in the subsequent code.

    :param lst: list of items to be permuted
    :return: a list of lists (one list per permutation)
    """
    # print(f'input_set[0]: {input_set[0]}')
    # print(f'input_set[1:]: {input_set[1:]}')

    if len(lst) == 0:
        return []

    elif len(lst) == 1:
        return [lst]

    result = []
    for i in range(len(lst)):
        first = lst[i]
        rest = lst[:i] + lst[i + 1:]
        for p in permutations(rest):
            perm = [first] + p
            result.append(perm)

    return result


def path_length(nodes, distances):
    """
    Compute the distance to travel across a list of cities (nodes) according to the matrix of distances between cities.

    :param nodes: list of cities (graph nodes)
    :param distances: matrix of distances between all pairs of cities
    :return:
    """
    path_len = 0
    for i in range(0, len(nodes) - 1):
        path_len += distances[nodes[i], nodes[i + 1]]
    return path_len


def day09():
    max_perm = 100000

    cities, distances = read_distances("2015/data/data_2015_09.txt")

    # print("\nCities:")
    # print(sorted(cities))

    # print("\nDistances: ")
    # print(distances)

    ncities = len(cities)
    # print(f'\tCities: {ncities}')
    nperm = factorial(ncities)
    #print(f'\tPermutations: {nperm}')
    if nperm > max_perm:
        print(f"Number of permutation exceeeds {max_perm}")
        exit()
    start = time()
    city_permutations = itertools.permutations(list(cities))
    print("Time taken for permutations:", time() - start)
    i = 0
    for perm in tqdm(city_permutations):
        i += 1
        l = path_length(perm, distances)
        if i == 1:
            shortest_dist = l
            longest_dist = l
        elif l < shortest_dist:
            shortest_dist = l
        elif l > longest_dist:
            longest_dist = l

        # print(f'\t{i}\t{l}\t{perm}')
    print("\n\nDay 09 - Part One")
    print(f"\tShortest distance: {shortest_dist}")

    print("\nDay 09 - Part Two")
    print(f"\tLongest distance: {longest_dist}")
