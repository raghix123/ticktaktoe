import openai
import re
client = openai.OpenAI(api_key="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")  # Put your actual key here


class GPTBot:

    def __init__(self, token):
        self.token = token
        

    def play(self, board):
        board_state = board.grid
        board_string = ','.join(f"'{x}'" for x in board_state)

        prompt = f""" You are playing Tic Tac Toe.

            Your token: {self.token}
            Opponent's token: {[c if c != ' ' else '_' for c in board.grid]}

            Board format:
            [0][1][2]
            [3][4][5]
            [6][7][8]

            Current board:
            {[c if c != ' ' else '_' for c in board.grid]}  # turns spaces into underscores for clarity

            Instructions:
            1. If you can win by playing one move, do it.
            2. If your opponent can win on their next move, block them.
            3. Otherwise, pick a strategic position (center, corners, etc.).

            ONLY return the number (0–8) where you want to move. No explanation. No punctuation. Just the number.
"""

        response = client.chat.completions.create(
            model="gpt-4o",  # ✅ Free plan model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=10,
            temperature=0
        )

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
