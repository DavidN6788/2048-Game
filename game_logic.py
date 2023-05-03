from tabulate import tabulate
import numpy as np
import math

class GameLogic:

    TILE_DISTRIBUTION = np.array([2, 2, 2, 2, 2, 2, 4, 4])

    def __init__(self, size=4):
        self._size = size
        self._board = np.zeros((self._size, self._size))
        self._initialize_board()
        # self._board = np.array([[2, 4, 8, 16], [4, 8, 16, 32], [8, 16, 32, 64], [16, 32, 64, 128]])

    def _initialize_board(self):
        starting_tiles = np.random.choice(GameLogic.TILE_DISTRIBUTION, 2)
        starting_row_col = np.random.randint(self._size, size=(2, 2))
        self._board[starting_row_col[0], starting_row_col[1]] = starting_tiles

    def print_board(self):
        table = tabulate(self._board, tablefmt="fancy_grid")
        print(table)

    def _shift_tiles_left(self):
        board = self._board
        result = np.zeros((self._size, self._size))
        r_index = 0
        for row_value in board:
            c_index = 0
            for col_value in row_value:
                if col_value != 0:
                    result[(r_index, c_index)] = col_value
                    c_index += 1
            r_index += 1
        self._board = result

    def _add_tiles(self):
        board = self._board
        for row_index in range(self._size):
            for col_index in range(self._size - 1):
                if board[(row_index, col_index + 1)] == board[(row_index, col_index)]:
                    board[(row_index, col_index)] += board[(row_index, col_index + 1)]
                    board[(row_index, col_index + 1)] = 0
        self._shift_tiles_left()

    def _insert_tile(self):
        board = self._board
        if np.any(board == 0):
            random_tile = np.random.choice(GameLogic.TILE_DISTRIBUTION, 1)
            index_of_zeros = np.argwhere(board == 0)
            random_row_col = index_of_zeros[np.random.randint(len(index_of_zeros))]
            board[random_row_col[0], random_row_col[1]] = random_tile[0]

    def move_left(self):
        self._shift_tiles_left()
        self._add_tiles()
        self._insert_tile()

    def move_right(self):
        self._board = np.fliplr(self._board)
        self.move_left()
        self._board = np.fliplr(self._board)

    def move_up(self):
        self._board = np.rot90(self._board, 1)
        self.move_left()
        self._board = np.rot90(self._board, -1)

    def move_down(self):
        self._board = np.rot90(self._board, -1)
        self.move_left()
        self._board = np.rot90(self._board, 1)

    def _game_lost(self):
        diff_rows = np.diff(self._board, axis=0)
        diff_columns = np.diff(self._board, axis=1)
        return False if np.any(diff_columns == 0) or np.any(diff_rows == 0) else True

    def _game_won(self):
        winning_tile = math.pow(2, self._size + 7)
        return True if np.any(self._board == winning_tile) else False

gl = GameLogic()
gl.print_board()
