from unittest import TestCase

from day_14_2015 import calc_distances


class Test(TestCase):
    def test_calc_distances(self):
        # Create a dataset with the example
        reindeers = dict()
        # Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
        reindeers['Comet'] = {"speed": 14, "run_time": 10, "rest_time": 127}
        # Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
        reindeers['Dancer'] = {"speed": 16, "run_time": 11, "rest_time": 162}

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
