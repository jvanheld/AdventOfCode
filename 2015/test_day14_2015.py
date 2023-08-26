from unittest import TestCase

from day14_2015 import calc_distances, calc_distance_profiles, calc_score_profiles


def create_test_dataset():
    """
    Create a dataset with the example

    :return: a dictionary where keys are reindeer names and values are dictionaries of running features
    (speed, run_time, rest_time)

    """

    reindeers = dict()
    # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    reindeers['Comet'] = {"speed": 14, "run_time": 10, "rest_time": 127}
    # Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
    reindeers['Dancer'] = {"speed": 16, "run_time": 11, "rest_time": 162}
    return reindeers


class Test(TestCase):

    def test_calc_distances(self):
        reindeers = create_test_dataset()
        # After one second, Comet has gone 14 km, while Dancer has gone 16 km.
        self.assertEqual({'Comet': 14, 'Dancer': 16}, calc_distances(reindeers, time=1))

        # After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km.
        self.assertEqual({'Comet': 140, 'Dancer': 160}, calc_distances(reindeers, time=10))

        # On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total
        # distance of 176 km.
        self.assertEqual({'Comet': 140, 'Dancer': 176}, calc_distances(reindeers, time=11))

        # In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km
        # (poor Dancer has only gotten 1056 km by that point).
        self.assertEqual({'Comet': 1120, 'Dancer': 1056}, calc_distances(reindeers, time=1000))

    def test_calc_distance_profiles(self):
        reindeers = create_test_dataset()
        dist_profiles = calc_distance_profiles(reindeers, time=1000)
        # print(dist_profiles)
        self.assertEqual([14, 16], list(dist_profiles[0]))
        self.assertEqual([140, 160], list(dist_profiles[9]))
        self.assertEqual([140, 176], list(dist_profiles[10]))
        self.assertEqual([1120, 1056], list(dist_profiles[999]))

    def test_calc_score_profiles(self):
        reindeers = create_test_dataset()
        dist_profiles = calc_distance_profiles(reindeers, time=1000)
        score_profiles = calc_score_profiles(dist_profiles)
        # after the 140th second, Comet pulls into the lead and gets his first point. Of course, since Dancer had been
        # in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.
        self.assertEqual([1, 139], list(score_profiles[139]))

        # After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312.
        # So, with the new scoring system, Dancer would win (if the race ended at 1000 seconds).
        self.assertEqual([312, 689], list(score_profiles[999]))
