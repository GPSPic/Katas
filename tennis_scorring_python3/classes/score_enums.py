from enum import Enum

class TennisScores(Enum):
    LOVE = ("Love", 0)
    FIFTEEN = ("Fifteen", 1)
    THIRTY = ("Thirty", 2)
    FORTY = ("Forty", 3)

    def __init__(self, display_value, points):
        self.display_value = display_value
        self.points = points