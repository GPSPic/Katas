import unittest

from classes.player import Player
from classes.game import Game

class TestPlayer(unittest.TestCase):
    
    def setUp(self):
        self.player1 = Player("Nadal")
        self.player2 = Player("Federer")
        self.current_game = Game(self.player1, self.player2)


# test 3: Player has a name
    def test_player_has_name(self):
        self.assertEqual("Nadal", self.player1.name)

#  test 4: Player score starts at 0
    def test_player_score_starts_at_0(self):
        self.assertEqual(0, self.player1.score)

# test 5: Player score can increase by increments of 1
    def test_player_score_on_increase(self):
        self.player1.score_point()
        self.assertEqual(1, self.player1.score)

# test 10: player can send updated score to their current game
    def test_player_can_send_score_to_current_game(self):
        self.player1.game = self.current_game
        self.assertEqual(0, self.player1.score)
        self.assertEqual(0, self.current_game.player1.score)
        self.player1.score_point()
        self.assertEqual(1, self.current_game.player1.score)