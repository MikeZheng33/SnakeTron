import pygame
from pygame.locals import *

from Entities import Entity, Agent, Player

FPS = 60
FramePerSec = pygame.time.Clock()

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BOARD_WIDTH = 20
BOARD_HEIGHT = 20


def main():
    pygame.init()
    surface = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("SnakeTron")

    clock = pygame.time.Clock()

    game_board = [[' ' for x in range(BOARD_HEIGHT)] for y in range(BOARD_WIDTH)]
    entities: list[Entity] = []

    center = (BOARD_WIDTH // 2, BOARD_HEIGHT // 2)
    entities.append(Player('1', [center]))
    game_board[center[0]][center[1]] = '1'

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        game_board = [[' ' for x in range(BOARD_HEIGHT)] for y in range(BOARD_WIDTH)]
        for entity in entities:
            if isinstance(entity, Agent):
                entity.move(game_board)
            for position in entity.get_positions():
                game_board[position[0]][position[1]] = entity.get_id()

        draw_board(surface, game_board)

        pygame.display.flip()
        clock.tick(1)


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
                case '1':
                    surface.fill(GREEN, pygame.Rect(i * block_width, j * block_height, block_width, block_height))
                case '2':
                    surface.fill(GREEN, pygame.Rect(i * block_width, j * block_height, block_width, block_height))


if __name__ == '__main__':
    main()
