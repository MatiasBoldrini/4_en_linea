

class PlayerWonException(Exception):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class WrongInputException(Exception):
    pass

class NoSpacesAvailableException(Exception):
    pass

class SpaceException(Exception):
    pass

class Board:
    def __init__(self):
        self.player1 = "🔴 "
        self.player2 = "🔵 "
        self.board = [["   " for i in range(8)] for j in range(8)]
        self.turn = True  # This var will be True if its player 1 turn.

    def available_spaces(self, column): 
        # get the amount of spaces available
        column_list = self.column_to_list(column)
        return len(list([i for i in column_list if i != "   "]))

    def insert_token(self, column):
        try:
            column = int(column)
            assert(0 <= column < 8)
        except (ValueError, AssertionError):
            raise WrongInputException()

        if not any("   " in row for row in self.board):
            raise NoSpacesAvailableException()
        amount_of_spaces_used = self.available_spaces(column)
        if amount_of_spaces_used > 7:
            raise SpaceException()
        row = 7 - amount_of_spaces_used

        self.board[row][column] = self.player1 if self.turn else self.player2

        self.check_list(self.column_to_list(column))  # check column
        self.check_list(self.board[row])  # check row
        self.check_list(self.SE_diagonal_to_list(row, column))
        self.check_list(self.NE_diagonal_to_list(row, column))
        self.turn = not self.turn

    def get_row(self,row): return self.board[row]
    def column_to_list(self, column):
        return [row[column] for row in self.board]

    def SE_diagonal_to_list(self, row, column):  # ↘ SE Diagonal
        # deviation from main diagonal
        increment = abs(row - column)
        row_increment = increment if row > column else 0
        col_increment = increment if column > row else 0
        # range delimiter to avoid IndexError on generator
        start_limit = max(0, min(row, column) - 3)
        end_limit = min(8 - increment, min(row, column) + 4)
        diagonal = [
            (self.board[i + row_increment][i + col_increment])
            for i in range(start_limit, end_limit)
        ]
        return diagonal

    def NE_diagonal_to_list(self, row, column):  # ↗ NE Diagonal
        increment = abs(7 - (row + column))
        diagonal = []
        if row + column > 7:
            diagonal = [(self.board[7 - i + increment][i]) for i in range(increment, 8)]
        else:
            diagonal = [
                (self.board[i][7 - i - increment]) for i in range(0, 8 - increment)
            ]

        return diagonal

    def check_list(self, list):
        # This is checking if the player has won.
        skin = self.player1 if self.turn else self.player2
        str_to_check = "".join(i for i in list)
        if skin * 4 in str_to_check:
            raise PlayerWonException("Player 1" if self.turn else "Player 2")
    
    def __str__(self):
        final_string = '+----'*8 + '+' + '\n'
        for i in self.board:
            for i in i:
                final_string += f'| {i}'
            final_string += '|' + '\n' + '+----'*8 + '+' + '\n'
        return final_string


if __name__ == "__main__":
    board = Board()
    
