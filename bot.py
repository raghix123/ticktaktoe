import random

class Bot:
    def __init__(self, token):
        self.token = token

    def play(self, board):
        # Pick a random number between (0,9)
        randomPosition = random.randrange(0,9)
        successful = board.markPlace(self.token, randomPosition)
        
        while successful == False:
            randomPosition = random.randrange(0,9)
            successful = board.markPlace(self.token, randomPosition)

        return randomPosition
        # Set it on the board using board.markPlace()