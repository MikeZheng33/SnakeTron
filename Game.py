import sys

import pygame
from pygame.locals import *

from Entities import Entity, Agent

FPS = 60
FramePerSec = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("SnakeTron")


def main():
    game_board = [[0 for x in range(20)] for y in range(20)]  # 20 by 20 array
    entities: list[Entity] = []
    pygame.init()
    while True:
        for entity in entities:
            if isinstance(entity, Agent):
                move(entity)
            for position in entity.get_position():
                game_board[position[0]][position[1]] = entity.id

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


def move(agent : Agent) -> str:
    pass


if __name__ == '__main__':
  main()