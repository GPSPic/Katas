from score_enums import TennisScores

class Game:
    def _init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.running_score = {
            "Player 1 score": 0, 
            "Player 2 score": 0
        }