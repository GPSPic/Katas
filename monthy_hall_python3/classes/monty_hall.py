from random import randint


class MontyHallGame:
    def __init__(self):
        self.prize = 1
        self.doors = [0,0,0]
        self.player_first_choice_value = None
        self.player_first_choice_index = None
        self.final_doors = [0,0]

# randomly assigns the prize value to one of the elements of the doors array
    def hide_prize(self):
        randomized = randint(0,2)
        self.doors[randomized] = self.prize

# saves the random door value and index choice of the player
    def choose_first_door(self):
        randomized = randint(0,2)
        self.player_first_choice_value = self.doors[randomized]
        self.player_first_choice_index = randomized
    
