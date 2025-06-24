class User:
    def __init__(self, token):
        self.token = token

    def play(self, board):
        while True:
            try:
                pos = 9
                while pos < 0 or pos > 8:
                    pos = int(input("Your move (0‑8): "))
                
                if board.markPlace(self.token, pos):
                    return pos
                print("Spot taken. Try again.")
            except ValueError:
                print("Enter a number between 0 and 8.")
