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
        self.board = [["   " for _ in range(8)] for _ in range(8)]
        self.turn = True  # This var will be True if its player 1 turn.

    def available_spaces(self, column): 
        # get the amount of spaces available
        column_list = self.column_to_list(column)
        return len([i for i in column_list if i != "   "])

    def insert_token(self, column):
        try:
            column = int(column)
            assert(0 <= column < 8)
        except (ValueError, AssertionError) as e:
            raise WrongInputException() from e

        if all("   " not in row for row in self.board):
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
        """
        It returns a list of the values of the squares in the SE diagonal of the board, starting from the
        square at the intersection of the row and column passed to the function, and going up to 4
        squares in either direction
        
        :param row: the row of the piece
        :param column: the column of the piece
        :return: A list of the values of the squares in the diagonal.
        """
        # deviation from main diagonal
        increment = abs(row - column)
        row_increment = increment if row > column else 0
        col_increment = increment if column > row else 0
        # range delimiter to avoid IndexError on generator
        start_limit = max(0, min(row, column) - 3)
        end_limit = min(8 - increment, min(row, column) + 4)
        return [(self.board[i + row_increment][i + col_increment]) for i in range(start_limit, end_limit)]

    def NE_diagonal_to_list(self, row, column):  # ↗ NE Diagonal
        # Checking the diagonal from the bottom left to the top right.
        increment = abs(7 - (row + column))
        diagonal = []
        if row + column > 7:
            return [(self.board[7 - i + increment][i]) for i in range(increment, 8)]
        else:
            return [self.board[i][7 - i - increment] for i in range(8 - increment)]

    def check_list(self, list):
        # This is checking if the player has won.
        skin = self.player1 if self.turn else self.player2
        str_to_check = "".join(list)
        if skin * 4 in str_to_check:
            raise PlayerWonException("Player 1" if self.turn else "Player 2")
    
    def __str__(self):
        # user friendly sudoku board
        final_string = '+----'*8 + '+' + '\n'
        for i in self.board:
            for i in i:
                final_string += f'| {i}'
            final_string += '|' + '\n' + '+----'*8 + '+' + '\n'
        return final_string


if __name__ == "__main__":
    board = Board()
    
