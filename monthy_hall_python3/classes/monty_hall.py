from random import randint


class MontyHallGame:
    def __init__(self, player, presenter, prize):
        self.player = player
        self.presenter = presenter
        self.prize = prize
        self.doors = [0,0,0]

    def hide_prize(self):
        randomized = randint(1,3)
        self.doors[randomized] = self.prize.value
    