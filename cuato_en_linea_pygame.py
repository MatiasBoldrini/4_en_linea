import pygame, sys
from cuatro_en_linea import *

class Color:
    black = (0, 0, 0)
    gray = (150, 150, 150)
    white = (255, 255, 255)
    blue = (20, 22, 29)
    player1 = (255, 0, 0)
    player2 = (253, 149, 9)


class Game:
    def __init__(self):

        self.board = Board()
        self.screen = pygame.display.set_mode((480, 550))
        self.screen.fill(Color.blue)
        pygame.init()

    def main(self):
        # This is the main loop of the game. It draws the grid, checks for mouse clicks, and updates
        # the screen.
        self.draw_grid()
        block_size = 60
        cursor_x = pygame.mouse.get_pos()[0] // block_size
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                try:
                    self.token_drop_animation(cursor_x)
                    self.board.insert_token(cursor_x)
                except PlayerWonException as Winner:
                    print("winner", Winner.name)
                except SpaceException:
                    print("Out of space. Try Again")
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

    def token_drop_animation(self, column):
        # This is the animation for the token drop. It draws a circle and updates the screen.
        token_size = 60
        range_top = (8 - self.board.available_spaces(column)) * 60
        clock = pygame.time.Clock()
        clock.tick(60)
        for i in range(token_size // 10, range_top // 10):
            color1 = Color.player1 if self.board.turn else Color.player2
            self.draw_grid()
            pygame.draw.circle(
                self.screen,
                color1,
                (column * token_size + token_size / 2, token_size / 2 + (i * 10)),
                17,
                0,
            )
            pygame.display.update()
        pygame.event.clear()

    def draw_grid(self):
        self.screen.fill(Color.blue)
        token_size = 60
        for x in range(8):
            for y in range(8):
                cursor_x = pygame.mouse.get_pos()[0] // token_size
                # get the current row of mouse_X -> 0..7
                pygame.draw.circle(
                    self.screen,
                    Color.player1 if self.board.turn else Color.player2,
                    (cursor_x * token_size + token_size / 2, token_size / 2),
                    17,
                    0,
                )
                # Checking if the current cell has something on it. If it does, it will draw a circle
                # with the color of the player that placed the token. If it doesn't, it will draw a
                # black circle.
                if not self.board.board[y][x].isspace():
                    color = (
                        Color.player1
                        if self.board.player1.strip() in self.board.board[y][x]
                        else Color.player2
                    )
                    pygame.draw.circle(
                        self.screen,
                        color,
                        (token_size * (x + 0.5), token_size * (y + 0.5) + token_size),
                        17,
                        0,
                    )
                else:
                    pygame.draw.circle(
                        self.screen,
                        Color.black,
                        (token_size * (x + 0.5), token_size * (y + 0.5) + token_size),
                        17,
                        0,
                    )

    def draw_text(self, text):
        font1 = pygame.font.SysFont("Jetbrains Mono", 25)
        img1 = font1.render(text, True, Color.gray)
        self.screen.blit(img1, (500, 20))
        pygame.display.update()

    def draw_play_again_button(self):
        # 550, 300, 180, 90
        font1 = pygame.font.SysFont("Jetbrains Mono", 20)
        img1 = font1.render("Play Again", True, Color.white)
        rect = img1.get_rect()
        pygame.draw.rect(img1, Color.player1, rect, 2)
        self.screen.blit(img1, (550, 300))
        pygame.display.update()


if __name__ == "__main__":
    a = Game()
    while True:
        a.main()
