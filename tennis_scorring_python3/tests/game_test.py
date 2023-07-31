import unittest

from classes.game import Game
from classes.player import Player

class TestGame(unittest.TestCase):

    def setUp(self):
        self.player1 = Player("Nadal")
