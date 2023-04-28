import numpy as np
from tabulate import tabulate

class GameLogic:

    TILE_DISTRIBUTION = np.array([2, 2, 2, 2, 2, 2, 4, 4])

    def __init__(self, size=4):
        self.size = size
        GameLogic.BOARD = np.zeros((self.size, self.size))
        self.initialize_board()

    def initialize_board(self):
        starting_tiles = np.random.choice(GameLogic.TILE_DISTRIBUTION, 2)
        starting_row_col = np.random.randint(self.size, size=(2, 2))
        GameLogic.BOARD[starting_row_col[0], starting_row_col[1]] = starting_tiles

    def printBoard(self):
        table = tabulate(GameLogic.BOARD, tablefmt="fancy_grid")
        print(table)

    def shift_tiles_left(self):
        board = GameLogic.BOARD
        result = np.zeros((self.size, self.size))
        r_index = 0
        for row_value in board:
            c_index = 0
            for col_value in row_value:
                if col_value != 0:
                    result[(r_index, c_index)] = col_value
                    c_index += 1
            r_index += 1
        GameLogic.BOARD = result

    def add_tiles(self):
        board = GameLogic.BOARD
        for row_index in range(self.size):
            for col_index in range(self.size - 1):
                if board[(row_index, col_index + 1)] == board[(row_index, col_index)]:
                    board[(row_index, col_index)] += board[(row_index, col_index + 1)]
                    board[(row_index, col_index + 1)] = 0
        self.shift_tiles_left()

    def insert_tile(self):
        board = GameLogic.BOARD
        if np.any(board == 0):
            random_tile = np.random.choice(self.TILE_DISTRIBUTION, 1)
            index_of_zeros = np.argwhere(board == 0)
            random_row_col = index_of_zeros[np.random.randint(len(index_of_zeros))]
            board[random_row_col[0], random_row_col[1]] = random_tile[0]

    def move_left(self):
        self.shift_tiles_left()
        self.add_tiles()
        self.insert_tile()
        self.printBoard()

    def move_right(self):
        GameLogic.BOARD = np.fliplr(GameLogic.BOARD)
        self.shift_tiles_left()
        self.add_tiles()
        self.insert_tile()
        GameLogic.BOARD = np.fliplr(GameLogic.BOARD)
        self.printBoard()

    def move_up(self):
        GameLogic.BOARD = np.rot90(GameLogic.BOARD, 1)
        self.shift_tiles_left()
        self.add_tiles()
        self.insert_tile()
        GameLogic.BOARD = np.rot90(GameLogic.BOARD, -1)
        self.printBoard()

    def move_down(self):
        GameLogic.BOARD = np.rot90(GameLogic.BOARD, -1)
        self.shift_tiles_left()
        self.add_tiles()
        self.insert_tile()
        GameLogic.BOARD = np.rot90(GameLogic.BOARD, 1)
        self.printBoard()

gl = GameLogic()
gl.printBoard()
