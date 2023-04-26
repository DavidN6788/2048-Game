import numpy as np
from tabulate import tabulate

class GameLogic:

    TILE_DISTRIBUTION = np.array([2, 2, 2, 2, 2, 2, 4, 4])

    def __init__(self, size=4):
        self.size = size
        GameLogic.BOARD = np.zeros((self.size, self.size))
        self.initialize_board()

    def initialize_board(self):
        # Generate two random tiles to start on the board
        starting_tiles = np.random.choice(GameLogic.TILE_DISTRIBUTION, 2)
        # Generate two random positions to place the starting tiles
        starting_row_col = np.random.randint(self.size, size=(2, 2))
        # Add the random tiles to the random positions
        GameLogic.BOARD[starting_row_col[0], starting_row_col[1]] = starting_tiles

    def printBoard(self):
        table = tabulate(GameLogic.BOARD, tablefmt="fancy_grid")
        print(table)

    def shift_tiles_left(self):
        board = GameLogic.BOARD
        result = np.zeros((self.size, self.size))
        r_index = 0
        for row_index, row_value in enumerate(board):
            c_index = 0
            for col_index, col_value in enumerate(row_value):
                if col_value != 0:
                    result[(r_index, c_index)] = col_value
                    c_index += 1
                    board[(row_index, col_index)] = 0
            r_index += 1
        GameLogic.BOARD = result

    def add_tiles(self):
        pass


gl = GameLogic()
gl.printBoard()
gl.shift_tiles_left()
gl.printBoard()
