from random import randint


class MontyHallGame:
    def __init__(self):
        self.prize = 1
        self.doors = [0,0,0]
        self.player_first_choice_value = None
        self.player_first_choice_index = None
        self.player_final_choice_value = None
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

#we hardcoded the player choice index in the final doors array. 
    def show_empty_door(self):
        if self.player_first_choice_value == 1:
            self.final_doors = [1,0]
        else:
            self.final_doors = [0,1]