import openai
import re
client = openai.OpenAI(api_key="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")  # Put your actual key here



class GPTBot:

    def __init__(self, token):
        self.token = token
        self.othertoken = "O"
        if self.token == "O":
            self.othertoken = "X"
        
        

    def play(self, board):
        board_state = board.grid
        board_string = ','.join(f"'{x}'" for x in board_state)

        prompt = f""" You are playing Tic Tac Toe.
        Tic Tac Toe is a game for two players who take turns placing their marks on a 3 by 3 grid. One player uses X, and the other uses O. The goal is to be the first to get three of your marks in a row. This row can be horizontal, vertical, or diagonal.

        Game setup:
            - The grid has nine spots numbered like this:

            0 | 1 | 2
            3 | 4 | 5
            6 | 7 | 8

            - Players choose a number to place their mark in the corresponding empty spot.
            - Players alternate turns, starting with X. On your turn, pick any empty spot and put your mark there.
            - After each move, check if the player has three marks in a row, collum, or diagnoally. If yes, that player wins.
            - If all spots are filled and no one has three in a row, the game is a draw.
            - The game ends when a player wins or when there are no empty spots left.

        Rules to play, always play in this order of priority. Thoroughly evaluate each rule before moving onto the next
            - If you can win by playing one move, you MUST play that move
            - If your opponent can win on their next move, YOU MUST BLOCK THEM
            - Otherwise, pick a strategic position (center, corners, etc.).

        My Game State:
            - Your token: {self.token}
            - Opponent's token: {self.othertoken}
            - Board format:
            [0][1][2]
            [3][4][5]
            [6][7][8]
            - Current board state:
            {board.grid[0]}|{board.grid[1]}|{board.grid[2]}
            ––––––
            {board.grid[3]}|{board.grid[4]}|{board.grid[5]}
            ––––––
            {board.grid[6]}|{board.grid[7]}|{board.grid[8]}

        Expected output:
            ONLY return the number (0–8) where you want to move. No explanation. No punctuation. Just the number.
            
"""
        print(prompt)

        response = client.chat.completions.create(
            model="gpt-4o",  # ✅ Free plan model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
            temperature=0
        )
        print(response)
        move_text = response.choices[0].message.content.strip()

        try:
        

            match = re.search(r"\b[0-8]\b", move_text)
            if match:
                move = int(match.group())
            else:
                print("⚠️ GPT gave invalid move:", move_text)
                return -1

            if board.markPlace(self.token, move):
                return move
            else:
                # fallback: pick first available
                for i in range(9):
                    if board.grid[i] == ' ':
                        board.markPlace(self.token, i)
                        return i
        except:
            print("⚠️ GPT gave invalid move:", move_text)
            return -1
