from cuatro_en_linea import *


class Terminal_game():
    def __init__(self): 
        self.board = Board()
    def play(self):
        while True:
            try:
                print(self.board)
                number = input('Input a number -> ')
                if number == 'exit':
                    raise ExitException()
                self.board.insert_token(number)
            except PlayerWonException as Player:
                print(f'{Player} Has Won!!')
                print(self.board)
                break
            except WrongInputException:
                print('Wrong Input. try again')
            except SpaceException:
                print('Out of Space!')
            except NoSpacesAvailableException:
                print('Tie. Game Over')
                break
            except ExitException:
                break
                
if __name__ == '__main__': # pragma: no cover
    terminal_game = Terminal_game()
    terminal_game.play()
        
