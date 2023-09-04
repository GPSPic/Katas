from classes.game_runner import GameRunner
import unittest

class GameRunnerTest(unittest.TestCase):

    def setUp(self):
        self.game_runner = GameRunner()

    def test_can_record_game_results(self):
        self.game_runner.run_multiple_games(1000)
        results = self.game_runner.results
        self.assertEqual(1000, len(results))