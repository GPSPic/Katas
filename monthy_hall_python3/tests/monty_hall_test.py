import unittest

from classes.player import Player
from classes.presenter import Presenter
from classes.prize import Prize
from classes.monty_hall import MontyHallGame

from functools import reduce
from operator import add

class MonthyHallTest(unittest.TestCase):
    def setUp(self):
        self.player = Player("Bob")
        self.presenter = Presenter("Tim")
        self.prize = Prize(100)
        self.monty_hall_game = MontyHallGame(self.player, self.presenter, self.prize)

    # test1: hide prize behind random door, verify value by checking total value of doors array elements
    def test_can_hide_prize_behind_doors(self):
        self.assertEqual(0, reduce(lambda a, b: a+b, self.monty_hall_game.doors))
        self.monty_hall_game.hide_prize()
        self.assertEqual(100, reduce(add, self.monty_hall_game.doors))
        self.assertEqual(100, sum(self.monty_hall_game.doors))

    # test2: 