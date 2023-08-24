"""
--- Day 14: Reindeer Olympics ---

This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their
energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole
seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.

Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.

After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km,
while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues
on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the
138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer
has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the
winning reindeer traveled?

Your puzzle answer was 2640.


--- Part Two ---

Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.

Instead, at the end of each second, he awards one point to the reindeer currently in the lead. (If there are multiple
reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit, of course,
as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point. He stays in
the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets
his first point. Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139
points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So,
with the new scoring system, Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points
does the winning reindeer have?


"""

import os

import numpy as np

from util import read_list


def calc_distance_profiles(reindeers: dict, time: int):
    """
    Compute the distance profile of a reindeer as a function of its running features (speed, run time, rest time).

    :param reindeer: a two-keys dictionary containing, for each reindeer, a dictionary with its features:
    "speed", "run_time" and "rest_time"
    :param time: time of the race
    :return: a numpy array with the distance done by each reindeer at each time point (second) of the race
    """
    dist_profiles = np.array([[0 for x in range(len(reindeers))] for y in range(time)])
    # dist_profiles = [[0 for x in range(len(reindeers))] for y in range(time)]
    # print(f"\n\nComputing distances")
    for i, reindeer in enumerate(reindeers):
        features = reindeers[reindeer]
        # print(f"\t{i}\t{reindeer}\t{features}")
        t = 0
        while t < time:
            run_time = min(features["run_time"], time - t)
            # print(f"\ttime: {time}\tt: {t}\trun_time: {run_time}")
            if run_time <= 0:
                break
            for j in range(1, run_time + 1):
                dist_profiles[t + j - 1][i] = dist_profiles[t - 1][i] + j * features["speed"]
            t += run_time
            rest_time = min(features["rest_time"], time - t)
            # print(f"\ttime: {time}\tt: {t}\trest_time: {rest_time}")
            if rest_time <= 0:
                break
            for j in range(1, rest_time + 1):
                dist_profiles[t + j - 1][i] = dist_profiles[t - 1][i]
            t += rest_time
    return dist_profiles


def calc_score_profiles(dist_profiles):
    """
    Given a distance profile matrix, compute a matrix with the number of points accumulated by each reindeer
    (columns) at each time point (rows).

    :param dist_profiles: distance profile matrix (2D numpy array with one row per time point and one column per
    reindeer)
    :return: a 2D numpy array with the same dimensions as tue dist_profile
    """

    # Compute a 1D array with the max distance at each time point
    max_per_time = dist_profiles.max(axis=1)

    # Compute a 2D array indicating which reindeer (column) has the max distance at each time point (row)
    nrow, ncol = np.shape(dist_profiles)
    is_max_at_time = np.array([[0 for x in range(ncol)] for y in range(nrow)])
    for i in range(nrow):
        for j in range(ncol):
            is_max_at_time[i][j] = dist_profiles[i][j] == max_per_time[i]

    # Compute the cumulated score profiles
    score_profiles = np.array([[0 for x in range(ncol)] for y in range(nrow)])
    for j in range(ncol):
        score_profiles[0][j] = is_max_at_time[0][j]
        for i in range(1, nrow):
            score_profiles[i][j] = score_profiles[i - 1][j] + is_max_at_time[i][j]

    return score_profiles


def calc_distances(reindeers: dict, time: int):
    dist = dict()
    # print(f"\n\nComputing distances")
    for reindeer in reindeers:
        features = reindeers[reindeer]
        # print(f"\t{reindeer}\t{features}")
        remaining = time
        dist[reindeer] = 0
        while remaining > 0:
            runtime = min(features["run_time"], remaining)
            dist[reindeer] += features["speed"] * runtime
            remaining -= runtime + features["rest_time"]
            # print(f"\t{reindeer}\tdist: {dist[reindeer]}\t{remaining}")
    # print(dist)
    return dist


def day14():
    data = read_list("2015/data/data_2015_day14.txt")
    # Dancer can fly 27 km/s for 5 seconds, but then must rest for 132 seconds.
    reindeers = dict()
    for line in data:
        items = line.strip().split()
        reindeers[items[0]] = {"speed": int(items[3]),
                               "run_time": int(items[6]),
                               "rest_time": int(items[13])}
    # print(reindeers)
    distances = calc_distances(reindeers, time=2503)
    print(f"\n\nDay 14 - Part One")
    print(f"\tBest distance\t{max(distances.values())}")

    distance_profiles = calc_distance_profiles(reindeers, time=2503)
    score_profiles = calc_score_profiles(distance_profiles)
    print(f"\n\nDay 14 - Part Two")
    # print(distance_profiles)
    # print(score_profiles)
    print(f"\tBest score\t{max(score_profiles[2502,])}")


if __name__ == '__main__':
    os.chdir('..')
    day14()
