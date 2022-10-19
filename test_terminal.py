import io
import unittest
from unittest.mock import patch

from cuatro_en_linea import Board
from cuatro_en_linea_game import Terminal_game


class Test_frontend(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Terminal_game()

    @patch("builtins.input", side_effect=["0", "0", "1", "1", "2", "2", "3", "exit"])
    def test_win_p1(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        print_output = fake_stdout.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['|', '+']) and i]
        self.assertEqual(print_statements[0], 'Player 1 Has Won!!')

    @patch("builtins.input", side_effect=["0", "0", "1", "1", "2", "2", "0", "3", "0", "3", "exit"])
    def test_win_p2(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        print_output = fake_stdout.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['|', '+']) and i]
        self.assertEqual(print_statements[0], 'Player 2 Has Won!!')

    @patch("builtins.input", side_effect=[
        "0", "1", "2", "3", "4", "5", "6", "7",
        "7", "6", "5", "4", "3", "2", "1", "0",
        "7", "6", "5", "4", "3", "2", "1", "0",
        "0", "1", "2", "3", "4", "5", "6", "7",
        "0", "1", "2", "3", "4", "5", "6", "7",
        "7", "6", "5", "4", "3", "2", "1", "0",
        "0", "1", "2", "3", "4", "5", "6", "7",
        "0", "1", "2", "3", "4", "5", "6", "7", "7","exit"])
    def test_tie(self,mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        print_output = fake_stdout.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['|', '+']) and i]
        self.assertEqual(print_statements[0], 'Tie. Game Over')

    @patch("builtins.input", side_effect=["0", "0", "0", "0", "0", "0", "0", "0", "0", "exit"])
    def test_out_of_space(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        print_output = fake_stdout.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['|', '+']) and i]
        self.assertEqual(print_statements[0], 'Out of Space!')

    @patch("builtins.input", side_effect=["exit"])
    def test_exit(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        print_output = fake_stdout.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['|', '+']) and i]
        self.assertFalse(print_statements)

    @patch("builtins.input", side_effect=["a", "10", "-1", "haosd", "<", "exit"])
    def test_bad_input(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        print_output = fake_stdout.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['|', '+']) and i]
        self.assertTrue(
            all(i == 'Wrong Input. try again' for i in print_statements))

    @patch("builtins.input", side_effect=["0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "exit"])
    def test_board(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        board_str = (
            "+----+----+----+----+----+----+----+----+\n"
            "| 🔵 | 🔴 |    |    |    |    |    |    |\n"
            "+----+----+----+----+----+----+----+----+\n"
            "| 🔴 | 🔵 |    |    |    |    |    |    |\n"
            "+----+----+----+----+----+----+----+----+\n"
            "| 🔵 | 🔴 |    |    |    |    |    |    |\n"
            "+----+----+----+----+----+----+----+----+\n"
            "| 🔴 | 🔵 |    |    |    |    |    |    |\n"
            "+----+----+----+----+----+----+----+----+\n"
            "| 🔵 | 🔴 |    |    |    |    |    |    |\n"
            "+----+----+----+----+----+----+----+----+\n"
            "| 🔴 | 🔵 |    |    |    |    |    |    |\n"
            "+----+----+----+----+----+----+----+----+\n"
            "| 🔵 | 🔴 |    |    |    |    |    |    |\n"
            "+----+----+----+----+----+----+----+----+\n"
            "| 🔴 | 🔵 |    |    |    |    |    |    |\n"
            "+----+----+----+----+----+----+----+----+\n"
        )

        self.assertIn(board_str, fake_stdout.getvalue())


if __name__ == "__main__": # pragma: no cover
    unittest.main()
