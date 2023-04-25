import numpy as np
from tabulate import tabulate

class GameLogic:

    TILE_DISTRIBUTION = np.array([2, 2, 2, 2, 2, 2, 4, 4])

    def __init__(self, size):
        self.size = size
        GameLogic.BOARD = np.zeros((self.size, self.size))
        self.initialize_board()

    def initialize_board(self):
        random_tile= GameLogic.TILE_DISTRIBUTION[np.random.randint(GameLogic.TILE_DISTRIBUTION.size)]
        random_row_col = np.random.randint(self.size, size=(1, 2))[0]
        GameLogic.BOARD[random_row_col[0], random_row_col[1]] = random_tile

    def printBoard(self):
        table = tabulate(GameLogic.BOARD, tablefmt="fancy_grid")
        print(table)

gl = GameLogic(4)
gl.printBoard()