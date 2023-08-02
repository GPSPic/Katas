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
        
    