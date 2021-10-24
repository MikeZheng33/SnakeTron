import pygame
from pygame.locals import *

from Entities import Entity, Agent

FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("SnakeTron")

    game_board = [[' ' for x in range(40)] for y in range(40)]  # 20 by 20 array
    entities: list[Entity] = []

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        # for entity in entities:
        #     entities.get_action(game_board) -> {'up', 'down', 'left', 'right'}

        draw_board(surface, game_board)

        pygame.display.flip()


def draw_board(surface, game_board):
    block_width = surface.get_width() // len(game_board)
    block_height = surface.get_height() // len(game_board[0])
    for i, row in enumerate(game_board):
        for j, square in enumerate(row):
            match square:
                case ' ':
                    surface.fill(BLACK, pygame.Rect(i * block_width, j * block_height, block_width, block_height))
                case '+':
                    surface.fill(RED, pygame.Rect(i * block_width, j * block_height, block_width, block_height))
                case '1h' | '1b':
                    surface.fill(GREEN, pygame.Rect(i * block_width, j * block_height, block_width, block_height))
                case '2h' | '2b':
                    surface.fill(GREEN, pygame.Rect(i * block_width, j * block_height, block_width, block_height))


if __name__ == '__main__':
    main()
