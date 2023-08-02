class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.running_score = {
            "Player 1 score": player1.score, 
            "Player 2 score": player2.score
        }

    def update_running_score(self):
        self.running_score["Player 1 score"] = self.player1.score
        self.running_score["Player 2 score"] = self.player2.score
        return self.declare_game()
    
    def declare_game(self):
        player1_score = self.running_score["Player 1 score"]
        player2_score = self.running_score["Player 2 score"]
        if player1_score > 3 and player1_score >= player2_score + 2:
            return f'Game {self.player1.name}'
        elif player2_score > 3 and player2_score >= player1_score + 2:
            return f'Game {self.player2.name}'
        else:
            return
        
    def announce_running_score(self):
        score = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        player1_score = self.running_score["Player 1 score"]
        player2_score = self.running_score["Player 2 score"]
        if player1_score == player2_score >= 3:
            return "Deuce"
        elif player1_score <= 3 and player2_score <= 3:
            return f'{score[player1_score]}, {score[player2_score]}'
        elif player1_score > 3 and player1_score >= player2_score + 2:
            return f'Game {self.player1.name}'
        elif player2_score > 3 and player2_score >= player1_score + 2:
            return f'Game {self.player2.name}'
        elif player1_score > 3 and player2_score == player1_score - 1:
            return f'Advantage {self.player1.name}'
        elif player2_score > 3 and player1_score == player2_score - 1:
            return f'Advantage {self.player2.name}'