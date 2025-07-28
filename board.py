import os
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'


class Board:

    def __init__(self):
        self.grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]

    def printBoard(self):
        # os.system('cls' if os.name == 'nt' else 'clear')
        print("Current Board (left)     |   Position Key (right)\n")

        for row in range(3):
            start = row * 3

            board_row = []
            key_row = []

            for i in range(3):
                val = self.grid[start + i]

                # Color the X and O
                if val == 'X':
                    display = f"{RED} X {RESET}"
                elif val == 'O':
                    display = f"{BLUE} O {RESET}"
                else:
                    display = "   "

                board_row.append(display)

                # Key: show index if empty
                if val == ' ':
                    key_row.append(f" {start + i} ")
                else:
                    key_row.append("   ")

            print(" |".join(board_row) +
                  "     |   " +
                  " |".join(key_row))

            if row < 2:
                print("---+---+---           ---+---+---")


    def checkState(self):
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6)] 
                
        # check for a win
        for a, b, c in wins:
            if self.grid[a] == self.grid[b] and self.grid[c] == self.grid[b] and self.grid[a] != ' ':
                return self.grid[a]
            
        # check for ongoing
        for x in self.grid:
            if (x == ' '):
                return 'ONGOING'

        #if its nothing else then its a tie        
        return 'TIE'         
    
    def markPlace(self, token, position):
        if self.grid[position] == ' ':
            self.grid[position] = token
            return True
        else:
            return False