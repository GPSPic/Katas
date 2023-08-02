import unittest

from classes.game import Game
from classes.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Nadal")
        self.player2 = Player("Federer")
        self.game = Game(self.player1, self.player2)

# test 6: game starts with scores of love/love
    def test_game_starts_with_0_score(self):
        self.assertEqual({
            "Player 1 score": 0, 
            "Player 2 score": 0
        }, 
        self.game.running_score)

# test 7: running score updates when updating player score
    def test_update_running_score(self):
        self.player1.score_point()
        self.game.update_running_score()
        self.assertEqual({
            "Player 1 score": 1, 
            "Player 2 score": 0
        }, 
        self.game.running_score)

# test 8: declare game won by player 1 if player 2 does not score
    def test_declare_player1_winner__with_no_player2_score(self):
        self.player1.score_point()
        self.player1.score_point()
        self.player1.score_point()
        self.player1.score_point()
        result = self.game.update_running_score()
        self.assertEqual(result, "Game Nadal")

# test 8: declare game won by player 2 if player 1 does not score
    def test_declare_player2_winner__with_no_player1_score(self):
        self.player2.score_point()
        self.player2.score_point()
        self.player2.score_point()
        self.player2.score_point()
        result = self.game.update_running_score()
        self.assertEqual(result, "Game Federer")