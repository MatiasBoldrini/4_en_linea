import unittest
from unittest.mock import patch
from cuatro_en_linea import *


class Test_logic(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_winner_horizontal(self):
        with self.assertRaises(PlayerWonException):
            for i in [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]:
                self.board.insert_token(i)

    def test_winner_vertical(self):
        with self.assertRaises(PlayerWonException):
            for i in [0, 1, 0, 1, 0, 1, 0]:
                self.board.insert_token(i)

    def test_column_to_list(self):

        for i in [0, 0, 0, 0, 0, 0, 0]:
            self.board.insert_token(i)
        self.assertEqual(
            self.board.column_to_list(0),
            ["   ", "🔴 ", "🔵 ", "🔴 ", "🔵 ", "🔴 ", "🔵 ", "🔴 "],
        )

    def test_winner_diagonal_NE(self):

        with self.assertRaises(PlayerWonException):
            self.board.board[5] = ["   ", "   ", "🔴 ", "🔴 ", "   ", "   ", "   ", "   "]
            self.board.board[6] = ["   ", "🔴 ", "   ", "🔴 ", "   ", "   ", "   ", "   "]
            self.board.board[7] = ["🔴 ", "   ", "   ", "🔵 ", "   ", "   ", "   ", "   "]
            self.board.insert_token(3)

    def test_diagonal_NE_list(self):

        with self.assertRaises(NoSpacesAvailableException):
            self.board.board = (["🔵 ", "🔴 ", "🔴 ", "🔵 ", "🔵 ", "🔴 ", "🔴 ", "🔵 "],)
            ["🔴 ", "🔵 ", "🔵 ", "🔴 ", "🔴 ", "🔵 ", "🔵 ", "🔴 "],
            ["🔵 ", "🔴 ", "🔴 ", "🔵 ", "🔵 ", "🔴 ", "🔴 ", "🔵 "],
            ["🔴 ", "🔵 ", "🔵 ", "🔴 ", "🔴 ", "🔵 ", "🔵 ", "🔴 "],
            ["🔵 ", "🔴 ", "🔴 ", "🔵 ", "🔵 ", "🔴 ", "🔴 ", "🔵 "],
            ["🔴 ", "🔵 ", "🔵 ", "🔴 ", "🔴 ", "🔵 ", "🔵 ", "🔴 "],
            ["🔵 ", "🔴 ", "🔴 ", "🔵 ", "🔵 ", "🔴 ", "🔴 ", "🔵 "],
            ["🔴 ", "🔵 ", "🔵 ", "🔴 ", "🔴 ", "🔵 ", "🔵 ", "🔴 "]
            for i in range(8):
                self.board.insert_token(i)

    def test_winner_horizontal_fake(self):

        for i in [0, 0, 1, 1, 2, 2, 5, 5]:
            self.board.insert_token(i)

    def test_winner_diagonal_fake(self):

        self.board.board = (["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],)
        ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
        ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
        ["   ", "   ", "   ", "   ", "🔴 ", "   ", "   ", "   "],
        ["   ", "   ", "   ", "   ", "🔵 ", "   ", "   ", "   "],
        ["   ", "   ", "🔴 ", "🔵 ", "🔴 ", "   ", "   ", "   "],
        ["   ", "🔴 ", "🔴 ", "🔴 ", "🔵 ", "   ", "   ", "   "],
        ["🔴 ", "🔵 ", "🔵 ", "🔵 ", "🔴 ", "   ", "   ", "🔵 "]

    def test_winner_diagonal_SE(self):

        with self.assertRaises(PlayerWonException):
            for i in [7, 7, 7, 6, 6, 5, 7, 5, 5, 6, 6, 4, 4, 4, 5, 0, 4]:
                self.board.insert_token(i)

    def test_list_diagonal_SE(self):

        for i in [7, 6, 6, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3, 3]:
            self.board.insert_token(i)
        self.assertEqual(self.board.SE_diagonal_to_list(7, 7), ["🔵 ", "🔵 ", "🔴 ", "🔴 "])

    def test_token_positions(self):

        for i in [7, 7, 7, 6, 6, 5, 7, 5, 5, 6, 6, 4, 4, 4, 5, 0]:
            self.board.insert_token(i)
        self.assertEqual(
            self.board.get_row(4), ["   ", "   ", "   ", "   ", "   ", "🔴 ", "🔴 ", "🔴 "]
        )
        self.assertEqual(
            self.board.get_row(5), ["   ", "   ", "   ", "   ", "🔵 ", "🔴 ", "🔵 ", "🔴 "]
        )
        self.assertEqual(
            self.board.get_row(6), ["   ", "   ", "   ", "   ", "🔴 ", "🔵 ", "🔴 ", "🔵 "]
        )
        self.assertEqual(
            self.board.get_row(7), ["🔵 ", "   ", "   ", "   ", "🔵 ", "🔵 ", "🔵 ", "🔴 "]
        )

    def test_overflow(self):

        with self.assertRaises(SpaceException):
            for _ in range(9):
                self.board.insert_token(0)

    def test_input_incorrect(self):

        with self.assertRaises(WrongInputException):
            self.board.insert_token("a")

    def test_input_bad_length(self):

        with self.assertRaises(WrongInputException):
            self.board.insert_token(8)

    def test_input_correct(self):

        self.board.insert_token(0)
        self.assertEqual(
            self.board.get_row(7),
            ["🔴 ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
        )

    def test_input_correct_string(self):

        self.board.insert_token("0")
        self.assertEqual(
            self.board.get_row(7),
            ["🔴 ", "   ", "   ", "   ", "   ", "   ", "   ", "   "],
        )


if __name__ == "__main__":
    unittest.main()
