import sys

import pygame
from pygame.locals import *

import Agent

FPS = 60
FramePerSec = pygame.time.Clock()

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(BLACK)
pygame.display.set_caption("SnakeTron")


class Game:
    game_board = [[0 for x in range(20)] for y in range(20)]  # 20 by 20 array
    agents = []
    pygame.init()
    while True:
        for agent in agents:
            for position in agent.getPosition():



        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
def handle_collision(agent1 : Agent, agent2 : Agent) -> bool:
    