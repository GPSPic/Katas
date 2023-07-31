import unittest

from classes.score_enums import TennisScores

class TestTennisScores(unittest.TestCase):

    def setUp(self):
        self.score0 = TennisScores.LOVE

# test 1: TennisScores Enum has display value
    def test_tennis_score_has_display_value(self):
        self.assertEqual("Love", self.score0.display_value)

# test 2: TennisScores Enum has points
    def test_tennis_score_has_points(self):
        self.assertEqual(0, self.score0.points)