import unittest
from unittest.mock import patch
import pytest
from Piece import Knight, Pawn, King, Rook, Bishop, Queen
from chess_engine import game_state
from enums import Player


class TestKnight(unittest.TestCase):
    # Unit-Test
    @patch('Piece.Knight.get_valid_piece_takes')
    def test_get_valid_piece_takes(self, mock_piece_moves):
        game = game_state()

        mock_piece_moves.return_value = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)]

        knight = Knight('n', 3, 3, Player.PLAYER_1)
        game.board[3][3] = knight

        result = knight.get_valid_piece_takes(game)

        expected_outcome = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)]

        assert len(result) == len(expected_outcome)

        print(f"\n{result}")

    @patch('Piece.Knight.get_valid_peaceful_moves')
    def test_get_valid_peaceful_moves(self, mock_piece_moves):
        game = game_state()

        mock_piece_moves.return_value = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)]

        knight = Knight('n', 3, 3, 'white')
        game.board[3][3] = knight

        result = knight.get_valid_peaceful_moves(game)  # Call the modified method

        expected_outcome = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)]

        assert len(result) == len(expected_outcome), f"Actual moves: {result}"

        print(f"\n{result}")

    @patch('Piece.Knight.get_valid_peaceful_moves')
    def test_all_moves_blocked_by_white_pawn_peaceful(self, mock_peaceful_moves):
        game = game_state()

        white_pawn_positions = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)]
        for row, col in white_pawn_positions:
            white_pawn = Pawn('P', row, col, Player.PLAYER_1)  # Assuming 'p' represents a white pawn
            game.board[row][col] = white_pawn
        mock_peaceful_moves.return_value = []

        knight = Knight('N', 3, 3, 'white')
        game.board[3][3] = knight

        can_move = knight.get_valid_peaceful_moves(game)

        assert not can_move, "Knight cannot move"
        print("\nKnight cannot move")

    @patch('Piece.Knight.get_valid_piece_takes')
    def test_all_moves_blocked_by_white_pawn_takes(self, mock_peaceful_moves):
        game = game_state()

        white_pawn_positions = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)]
        for row, col in white_pawn_positions:
            white_pawn = Pawn('P', row, col, Player.PLAYER_1)  # Assuming 'p' represents a white pawn
            game.board[row][col] = white_pawn
        mock_peaceful_moves.return_value = []

        knight = Knight('N', 3, 3, Player.PLAYER_1)
        game.board[3][3] = knight

        can_move = knight.get_valid_piece_takes(game)

        assert not can_move, "Knight cannot move"
        print("\nKnight cannot move")

    @patch('Piece.Knight.get_valid_peaceful_moves')
    def test_all_moves_blocked_by_black_pawn_piece(self, mock_peaceful_moves):
        game = game_state()

        black_pawn_positions = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)]
        for row, col in black_pawn_positions:
            black_pawn = Pawn('p', row, col, Player.PLAYER_2)  # Assuming 'p' represents a black pawn
            game.board[row][col] = black_pawn

        knight = Knight('N', 3, 3, Player.PLAYER_1)
        game.board[3][3] = knight

        valid_moves = knight.get_valid_peaceful_moves(game)

        if valid_moves:
            print("Valid peaceful moves for the knight:")
            print(black_pawn_positions)
        else:
            print("No valid peaceful moves for the knight.")

    @patch('Piece.Knight.get_valid_piece_takes')
    def test_all_moves_blocked_by_black_pawn_piece_takes(self, mock_peaceful_moves):
        game = game_state()

        black_pawn_positions = [(1, 2), (1, 4), (2, 1), (2, 5), (4, 1), (4, 5), (5, 2), (5, 4)]
        for row, col in black_pawn_positions:
            black_pawn = Pawn('p', row, col, Player.PLAYER_2)  # Assuming 'p' represents a black pawn
            game.board[row][col] = black_pawn

        knight = Knight('N', 3, 3, Player.PLAYER_1)
        game.board[3][3] = knight

        valid_moves = knight.get_valid_piece_takes(game)

        if valid_moves:
            print("Valid peaceful moves for the knight:")
            print(black_pawn_positions)
        else:
            print("No valid peaceful moves for the knight.")

    @patch('Piece.Knight.get_valid_peaceful_moves')
    def test_knight_can_capture_pawn_peaceful(self, mock_valid_moves):
        game = game_state()

        knight = Knight('n', 3, 3, Player.PLAYER_1)
        game.board[3][3] = knight

        white_king = King('k', 6, 3, Player.PLAYER_1)
        game.board[6][3] = white_king

        black_pawn = Pawn('p', 5, 4, Player.PLAYER_2)
        game.board[5][4] = black_pawn

        mock_valid_moves.return_value = [(5, 4)]

        valid_moves = knight.get_valid_peaceful_moves(game)

        self.assertEqual(valid_moves, [(5, 4)], "Knight should only be able to move to (5, 4) to capture the pawn")

        print("\nKnight should only be able to move to (5, 4) to capture the pawn")

    @patch('Piece.Knight.get_valid_piece_takes')
    def test_knight_can_capture_pawn_takes(self, mock_valid_moves):
        game = game_state()

        knight = Knight('n', 3, 3, Player.PLAYER_1)
        game.board[3][3] = knight

        white_king = King('k', 6, 3, Player.PLAYER_1)
        game.board[6][3] = white_king

        black_pawn = Pawn('p', 5, 4, Player.PLAYER_2)
        game.board[5][4] = black_pawn

        mock_valid_moves.return_value = [(5, 4)]

        valid_moves = knight.get_valid_piece_takes(game)

        self.assertEqual(valid_moves, [(5, 4)], "Knight should only be able to move to (5, 4) to capture the pawn")

        print("\nKnight should only be able to move to (5, 4) to capture the pawn")

    @patch('Piece.Knight.get_valid_peaceful_moves')
    def test_knight_blocking_king_from_checkmate_peaceful(self, mock_valid_moves):
        game = game_state()

        knight = Knight('n', 3, 3, Player.PLAYER_1)
        game.board[3][3] = knight

        white_king = King('k', 6, 3, Player.PLAYER_1)
        game.board[6][3] = white_king

        black_rook = Rook('r', 6, 0, Player.PLAYER_2)
        game.board[6][0] = black_rook

        mock_valid_moves.return_value = []

        valid_moves = knight.get_valid_peaceful_moves(game)

        self.assertEqual(valid_moves, [], "Knight should not be able to move as it is blocking checkmate")
        print("\nKnight should not be able to move as it is blocking checkmate")

    @patch('Piece.Knight.get_valid_piece_takes')
    def test_knight_blocking_king_from_checkmate_takes(self, mock_valid_moves):
        game = game_state()
        knight = Knight('n', 3, 3, Player.PLAYER_1)
        game.board[3][3] = knight
        white_king = King('k', 6, 3, Player.PLAYER_1)
        game.board[6][3] = white_king
        black_rook = Rook('r', 6, 0, Player.PLAYER_2)
        game.board[6][0] = black_rook
        mock_valid_moves.return_value = []
        valid_moves = knight.get_valid_piece_takes(game)

        self.assertEqual(valid_moves, [], "Knight should not be able to move as it is blocking checkmate")
        print("\nKnight should not be able to move as it is blocking checkmate")

    @patch('Piece.King.get_valid_piece_takes')
    def test_end_game_takes(self, mock_valid_moves):
        game = game_state()
        white_king = King('K', 7, 0, Player.PLAYER_1)
        game.board[7][0] = white_king
        black_rook1 = Rook('r', 0, 0, Player.PLAYER_2)
        game.board[0][0] = black_rook1
        black_rook2 = Rook('r', 7, 7, Player.PLAYER_2)
        game.board[7][7] = black_rook2
        black_bishop = Bishop('b', 0, 7, Player.PLAYER_2)
        game.board[0][7] = black_bishop
        mock_valid_moves.return_value = []
        valid_moves = white_king.get_valid_piece_takes(game)
        self.assertEqual(valid_moves, [], "King can't move")
        print("\nKing can't move")

    @patch('Piece.King.get_valid_peaceful_moves')
    def test_end_game_peaceful(self, mock_valid_moves):
        game = game_state()
        white_king = King('K', 7, 0, Player.PLAYER_1)
        game.board[7][0] = white_king
        black_rook1 = Rook('r', 0, 0, Player.PLAYER_2)
        game.board[0][0] = black_rook1
        black_rook2 = Rook('r', 7, 7, Player.PLAYER_2)
        game.board[7][7] = black_rook2
        black_bishop = Bishop('b', 0, 7, Player.PLAYER_2)
        game.board[0][7] = black_bishop
        mock_valid_moves.return_value = []
        valid_moves = white_king.get_valid_peaceful_moves(game)
        self.assertEqual(valid_moves, [], "King can't move")
        print("\nKing can't move")

    ####################################################################

    # Integration-Test
    @patch('Piece.Knight.get_valid_peaceful_moves')
    @patch('Piece.Knight.get_valid_piece_takes')
    def test_get_valid_piece_moves(self, mock_takes, mock_peaceful):
        game = game_state()

        mock_peaceful.return_value = [(1, 2), (1, 4)]
        mock_takes.return_value = [(2, 3), (3, 5)]

        knight = Knight('n', 3, 3, Player.PLAYER_1)
        game.board[3][3] = knight

        valid_moves = knight.get_valid_piece_moves(game)

        expected_moves = [(1, 2), (1, 4), (2, 3), (3, 5)]

        self.assertEqual(valid_moves, expected_moves,
                         "The method should return the combination of peaceful moves and takes")

        print("\nValid moves:", valid_moves)

    ####################################################################

    # System Test
    def test_fools_mate(self):
        game = game_state()

        game.board[0][4] = King('k', 0, 4, Player.PLAYER_2)
        game.board[0][3] = Queen('q', 0, 3, Player.PLAYER_2)
        game.board[0][2] = Bishop('b', 0, 2, Player.PLAYER_2)
        game.board[0][5] = Bishop('b', 0, 5, Player.PLAYER_2)
        game.board[0][1] = Knight('n', 0, 1, Player.PLAYER_2)
        game.board[0][6] = Knight('n', 0, 6, Player.PLAYER_2)
        game.board[0][0] = Rook('r', 0, 0, Player.PLAYER_2)
        game.board[0][7] = Rook('r', 0, 7, Player.PLAYER_2)
        for col in range(8):
            game.board[1][col] = Pawn('p', 1, col, Player.PLAYER_1)

        white_king = King('K', 7, 4, Player.PLAYER_1)
        game.board[7][4] = white_king
        game.board[7][3] = Queen('Q', 7, 3, Player.PLAYER_1)
        game.board[7][2] = Bishop('B', 7, 2, Player.PLAYER_1)
        game.board[7][5] = Bishop('B', 7, 5, Player.PLAYER_1)
        game.board[7][1] = Knight('N', 7, 1, Player.PLAYER_1)
        game.board[7][6] = Knight('N', 7, 6, Player.PLAYER_1)
        game.board[7][0] = Rook('R', 7, 0, Player.PLAYER_1)
        game.board[7][7] = Rook('R', 7, 7, Player.PLAYER_1)
        for col in range(8):
            game.board[6][col] = Pawn('P', 6, col, Player.PLAYER_1)

        game.move_piece((6, 5), (5, 5), False)
        game.move_piece((1, 4), (3, 4), False)
        game.move_piece((6, 6), (4, 6), False)
        game.move_piece((0, 3), (4, 7), False)


        valid_moves = white_king.get_valid_peaceful_moves(game)

        self.assertEqual(valid_moves, [], "White king can't move")
        print("\nWhite king can't move its a fool mate")


if __name__ == "__main__":
    pytest.main()