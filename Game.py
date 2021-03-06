import random

import pygame
from pygame.locals import *

from Entities import Entity, Agent, Player, AI

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

BOARD_WIDTH = 20
BOARD_HEIGHT = 20


def main():
    pygame.init()
    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("SnakeTron")

    clock = pygame.time.Clock()

    game_board = [[' ' for x in range(BOARD_HEIGHT)] for y in range(BOARD_WIDTH)]
    entities: list[Entity] = []

    apple_invalid = True
    apple_pos = 0, 0

    player_pos = 4, 4
    entities.append(Player('1', [player_pos]))
    game_board[player_pos[0]][player_pos[1]] = '1'

    ai_pos = 14, 14
    entities.append(AI('2', [ai_pos]))
    game_board[ai_pos[0]][ai_pos[1]] = '2'

    frame_count: int = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                for entity in entities:
                    if isinstance(entity, Player):
                        entity.update_control(event.key)
            elif event.type == QUIT:
                return
                
        if not frame_count:
            for entity in entities:
                if isinstance(entity, Agent):
                    moved: str = entity.move(game_board)
                    if moved == 'apple':
                        apple_invalid = True
                    elif 'lose' in moved:
                        return
            game_board = [[' ' for x in range(BOARD_HEIGHT)] for y in range(BOARD_WIDTH)]

            if apple_invalid:
                apple_pos = random_apple(game_board)
                apple_invalid = False
            game_board[apple_pos[0]][apple_pos[1]] = '+'

            for entity in entities:
                for position in entity.get_positions():
                    game_board[position[0]][position[1]] = entity.get_id()
            draw_board(surface, game_board)
            pygame.display.flip()

        frame_count += 1
        if frame_count == 15:
            frame_count = 0
        clock.tick(120)


def random_apple(game_board, range_x=None, range_y=None) -> tuple[int, int]:
    if range_x is None:
        range_x = range(0, BOARD_WIDTH)
    if range_y is None:
        range_y = range(0, BOARD_HEIGHT)

    empty_positons = [(x, y) for x in range_x for y in range_y if game_board[x][y] == ' ']

    return random.choice(empty_positons)


def random_position(range_x=None, range_y=None) -> tuple[int, int]:
    if range_x is None:
        range_x = range(0, BOARD_WIDTH)
    if range_y is None:
        range_y = range(0, BOARD_HEIGHT)
    return random.choice(range_x), random.choice(range_y)


def draw_board(surface, game_board):
    block_width = surface.get_width() // len(game_board)
    block_height = surface.get_height() // len(game_board[0])
    for i, row in enumerate(game_board):
        for j, square in enumerate(row):
            x = i
            y = j + 1
            if square == ' ':
                surface.fill(BLACK, pygame.Rect(x * block_width, SCREEN_HEIGHT - y * block_height,
                                                block_width, block_height))
            elif square == '+':
                surface.fill(RED, pygame.Rect(x * block_width, SCREEN_HEIGHT - y * block_height,
                                              block_width, block_height))
            elif square == '1':
                surface.fill(GREEN, pygame.Rect(x * block_width, SCREEN_HEIGHT - y * block_height,
                                                block_width, block_height))
            elif square == '2':
                surface.fill(BLUE, pygame.Rect(x * block_width, SCREEN_HEIGHT - y * block_height,
                                                block_width, block_height))


if __name__ == '__main__':
    main()
