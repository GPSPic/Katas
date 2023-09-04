import unittest

from archived.prize import Prize
from classes.monty_hall import MontyHallGame

from functools import reduce
from operator import add

class MonthyHallTest(unittest.TestCase):
    def setUp(self):
        self.monty_hall_game = MontyHallGame()

    # test1: hide prize behind random door, verify value by checking total value of doors array elements
    def test_can_hide_prize_behind_doors(self):
        self.assertEqual(0, reduce(lambda a, b: a+b, self.monty_hall_game.doors))
        self.monty_hall_game.hide_prize()
        self.assertEqual(1, reduce(add, self.monty_hall_game.doors))
        self.assertEqual(1, sum(self.monty_hall_game.doors))

    # test2: player picks a door
    def test_player_can_choose_a_door(self):
        self.assertEqual(False, type(self.monty_hall_game.player_first_choice_value) is int)
        self.assertEqual(None, self.monty_hall_game.player_first_choice_index)
        self.monty_hall_game.choose_first_door()
        result = type(self.monty_hall_game.player_first_choice_value) is int
        self.assertEqual(True, result)
        self.assertEqual(True, isinstance(self.monty_hall_game.player_first_choice_index, int))

    # test 