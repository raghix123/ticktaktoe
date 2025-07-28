#!/python
import time
from board import Board
from bot import Bot
from user import User
from sbot import Sbot
from gptbot import GPTBot

def main():
    board = Board()

    player = User('X')
    botY = GPTBot('O')

    # while True:
    #     botX.play()
    #     board.checkState()

    while board.checkState() == 'ONGOING':
        position = player.play(board)
        board.printBoard()
        result = board.checkState()
        if result in ['X','TIE']:
            print(f"Game Over X: {result}")
            quit()
        print("\n\n")

        position = botY.play(board)
        time.sleep(2)
        board.printBoard()
        result = board.checkState()
        if result in ['O','TIE']:
            print(f"Game Over Y: {result}")
            quit()
        print("\n\n")

if __name__ == '__main__':
    main()

