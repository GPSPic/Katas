import unittest

from classes.player import Player

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player1 = Player("Nadal")

# test 3: Player has a name
    def test_player_has_name(self):
        self.assertEqual("Nadal", self.player1.name)

#  test 4: Player score starts at 0
    def test_player_score_starts_at_0(self):
        self.assertEqual(0, self.player1.score)

# test 5: Player score can increase by increments of 1
    def test_player_score_cn_increase(self):
        self.player1.score_point()
        self.assertEqual(1, self.player1.score)