import random

class Sbot:
    def __init__(self, token):
        self.token = token
        self.otherToken = 'X'
        if (self.token == 'X'   ):
            self.otherToken = 'O'

    def play(self, board):

        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)] 
        
        for a, b, c in wins:
            cells = [board.grid[a], board.grid[b], board.grid[c]]
            if cells.count(self.token) == 2 and cells.count(' ') == 1:
                if board.grid[a] == ' ':
                    board.markPlace(self.token, a)
                    return a
                elif board.grid[b] == ' ':
                    board.markPlace(self.token, b)
                    return b
                elif board.grid[c] == ' ':
                    board.markPlace(self.token, c)
                    return c

        for a, b, c in wins:
            cells = [board.grid[a], board.grid[b], board.grid[c]]
            if cells.count(self.otherToken) == 2 and cells.count(' ') == 1:
                if board.grid[a] == ' ':
                    board.markPlace(self.token, a)
                    return a
                elif board.grid[b] == ' ':
                    board.markPlace(self.token, b)
                    return b
                elif board.grid[c] == ' ':
                    board.markPlace(self.token, c)
                    return c



        # Pick a random number between (0,9)
        randomPosition = random.randrange(0,9)
        successful = board.markPlace(self.token, randomPosition)
        
        while successful == False:
            randomPosition = random.randrange(0,9)
            successful = board.markPlace(self.token, randomPosition)

        return randomPosition
        # Set it on the board using board.markPlace()