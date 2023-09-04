from classes.monty_hall import MontyHallGame

class GameRunner:
    def __init__(self):
        self.win_percentage = 0
        self.results = []
        # self.game_example = MontyHallGame()

    def run_multiple_games_with_swap_last_door(self, n):
        number_of_wins = 0
        for i in range(n):
            game_example = MontyHallGame()
            game_example.run_game(True)
            self.results.append(game_example.player_final_choice_value)
            if game_example.player_final_choice_value == 1:
                number_of_wins += 1
        self.win_percentage = number_of_wins / n * 100
      
    
    def run_multiple_games_without_swap_last_door(self, n):
        i = n
        number_of_wins = 0
        while n > 0:
            game_example = MontyHallGame()
            game_example.run_game(False)
            self.results.append(game_example.player_final_choice_value)
            if game_example.player_final_choice_value == 1:
                number_of_wins += 1
            n-=1
        self.win_percentage = number_of_wins / i * 100

