from cuatro_en_linea import *

class Terminal_game():
    def __init__(self): 
        self.board = Board()
    def play(self):
        while True:
            try:
                number = input('Input a number -> ')
                self.board.insert_token(number)
                print(self.board)
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
                
    

if __name__ == '__main__':
    terminal_game = Terminal_game()
    terminal_game.play()
        
