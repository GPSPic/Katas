from classes.game_runner import GameRunner
import unittest

class GameRunnerTest(unittest.TestCase):

    def setUp(self):
        self.game_runner = GameRunner()

    # def test_can_record_game_results_when_swapping_last_door(self):
    #     self.game_runner.run_multiple_games_with_swap_last_door(10)
    #     results = self.game_runner.results
    #     self.assertEqual(1000, len(results))

    def test_can_record_game_results_when_not_swapping(self):
        self.game_runner.run_multiple_games_without_swap_last_door(10)
        self.assertEqual(10, len(self.game_runner.results))

    def test_calculate_win_percentage_when_swapping(self):
        self.game_runner.run_multiple_games_with_swap_last_door(1000000)
        print(f'Swap the door: {self.game_runner.win_percentage}%')
        # self.assertAlmostEqual(self.game_runner.win_percentage, 66.7, 2, "Aaaaaah")

    def test_calculate_win_percentage_when_keeping(self):
        self.game_runner.run_multiple_games_without_swap_last_door(1000000)
        print(f'Keep the door: {self.game_runner.win_percentage}%')