from tabulate import tabulate
import numpy as np
import math

class GameLogic:

    TILE_DISTRIBUTION = np.array([2, 2, 2, 2, 2, 2, 4, 4])

    def __init__(self, size=4):
        self._size = size
        self._board = self._initialize_board()
        self._previous_board = self._board

    @property
    def board(self):
        self._print_board(self._board)
        return self._board

    @property
    def previous_board(self):
        self._print_board(self._previous_board)
        return self._previous_board

    def _initialize_board(self):
        board = np.zeros((self._size, self._size))
        starting_tiles = np.random.choice(GameLogic.TILE_DISTRIBUTION, 2)
        starting_row_col = np.random.randint(self._size, size=(2, 2))
        board[starting_row_col[0], starting_row_col[1]] = starting_tiles
        return board

    def _print_board(self, board):
        table = tabulate(board, tablefmt="fancy_grid")
        print(table)

    def _shift_tiles_left(self, board):
        result = np.zeros((self._size, self._size))
        r_index = 0
        for row_value in board:
            c_index = 0
            for col_value in row_value:
                if col_value != 0:
                    result[(r_index, c_index)] = col_value
                    c_index += 1
            r_index += 1
        return result

    def _add_tiles(self, board):
        for row_index in range(self._size):
            for col_index in range(self._size - 1):
                if board[(row_index, col_index + 1)] == board[(row_index, col_index)]:
                    board[(row_index, col_index)] += board[(row_index, col_index + 1)]
                    board[(row_index, col_index + 1)] = 0
        return self._shift_tiles_left(board)

    def _insert_tile(self, board):
        if np.any(board == 0):
            random_tile = np.random.choice(GameLogic.TILE_DISTRIBUTION, 1)
            index_of_zeros = np.argwhere(board == 0)
            random_row_col = index_of_zeros[np.random.randint(len(index_of_zeros))]
            board[random_row_col[0], random_row_col[1]] = random_tile[0]
        return board

    def move_left(self):
        current_board = self._board
        self._previous_board = current_board
        shift_board_left = self._shift_tiles_left(current_board)
        add_board = self._add_tiles(shift_board_left)
        insert_board = self._insert_tile(add_board)
        self._board = insert_board

    def move_right(self):
        current_board = self._board
        self._previous_board = current_board
        flip_board_one = np.fliplr(current_board)
        shift_board_left = self._shift_tiles_left(flip_board_one)
        add_board = self._add_tiles(shift_board_left)
        insert_board = self._insert_tile(add_board)
        flip_board_two = np.fliplr(insert_board)
        self._board = flip_board_two

    def move_up(self):
        current_board = self._board
        self._previous_board = current_board
        rotate_board_one = np.rot90(current_board, 1)
        shift_board_left = self._shift_tiles_left(rotate_board_one)
        add_board = self._add_tiles(shift_board_left)
        insert_board = self._insert_tile(add_board)
        rotate_board_two = np.rot90(insert_board, -1)
        self._board = rotate_board_two

    def move_down(self):
        current_board = self._board
        self._previous_board = current_board
        rotate_board_one = np.rot90(current_board, -1)
        shift_board_left = self._shift_tiles_left(rotate_board_one)
        add_board = self._add_tiles(shift_board_left)
        insert_board = self._insert_tile(add_board)
        rotate_board_two = np.rot90(insert_board, 1)
        self._board = rotate_board_two

    def _game_lost(self):
        diff_rows = np.diff(self._board, axis=0)
        diff_columns = np.diff(self._board, axis=1)
        return False if np.any(diff_columns == 0) or np.any(diff_rows == 0) else True

    def _game_won(self):
        winning_tile = math.pow(2, self._size + 7)
        return True if np.any(self._board == winning_tile) else False

gl = GameLogic()
gl.board
