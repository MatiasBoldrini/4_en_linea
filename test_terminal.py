import io
import unittest
from pprint import pprint
from unittest.mock import patch

from cuatro_en_linea import Board, PlayerWonException
from cuatro_en_linea_game import Terminal_game


class Test_frontend(unittest.TestCase):
    def setUp(self):
        self.board = Board()
        self.game = Terminal_game()

    @patch(
        "builtins.input",
        side_effect=["0", "0", "1", "1", "2", "2", "3", "exit"],
    )
    def test_win(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        print_output = fake_stdout.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['|', '+']) and i]
        self.assertEqual(print_statements[0], 'Player 1 Has Won!!')
    @patch(
        "builtins.input",
        side_effect=["0","0", "0", "0", "0","0", "0", "0", "0", "exit"],
    )
    def test_out_of_space(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        print_output = fake_stdout.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['|', '+']) and i]
        self.assertEqual(print_statements[0], 'Out of Space!')
    @patch(
        "builtins.input",
        side_effect=["a","10","-1","haosd", "<", "exit"],
    )
    def test_bad_input(self, mock_inputs):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            self.game.play()
        print_output = fake_stdout.getvalue().split('\n')
        print_statements = [i for i in print_output
                            if not any(j in i for j in ['|', '+']) and i]
        self.assertTrue(all(i == 'Wrong Input. try again' for i in print_statements))

if __name__ == "__main__":
    unittest.main()
# self.board_0 = (
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#         )
#         board_1 = (
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "|    |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n"
#             "| 🔴 |    |    |    |    |    |    |    |\n"
#             "+----+----+----+----+----+----+----+----+\n")
