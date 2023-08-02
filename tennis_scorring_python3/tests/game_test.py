import unittest

from classes.game import Game
from classes.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Nadal")
        self.player2 = Player("Federer")
        self.game = Game(self.player1, self.player2)
        self.player1.game = self.game
        self.player2.game = self.game

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

# test 9: declare game won by player 2 if player 1 does not score
    def test_declare_player2_winner__with_no_player1_score(self):
        self.player2.score_point()
        self.player2.score_point()
        self.player2.score_point()
        self.player2.score_point()
        result = self.game.update_running_score()
        self.assertEqual(result, "Game Federer")

# test 11: annonce score each time a point is scored and player 2 wins
    def test_can_announce_running_score(self):
        self.player1.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Fifteen, Love")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Fifteen, Fifteen")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Fifteen, Thirty")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Fifteen, Forty")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Game Federer")

# test 11: annonce score each time a point is scored and player 2 wins after deuce
    def test_can_announce_running_score(self):
        self.player1.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Fifteen, Love")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Fifteen, Fifteen")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Fifteen, Thirty")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Fifteen, Forty")
        self.player1.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Thirty, Forty")
        self.player1.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Deuce")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Advantage Federer")
        self.player1.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Deuce")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Advantage Federer")
        self.player2.score_point()
        result = self.game.announce_running_score()
        self.assertEqual(result, "Game Federer")