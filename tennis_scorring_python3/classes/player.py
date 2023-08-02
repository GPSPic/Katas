class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.game = None

    def score_point(self):
        self.score = self.score + 1
        if self.game != None:
            self.game.update_running_score()
        