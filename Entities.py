import pygame
from pygame.locals import *


class Entity:
    def __init__(self, identifier: str, positions: list):
        self._identifier = identifier
        self._positions = positions

    def get_id(self):
        return self._identifier

    def get_positions(self):
        return self._positions

    def set_positions(self, value):
        self._positions = value


class Apple(Entity):
    def __init__(self, positions):
        super().__init__('+', positions)


class Agent(Entity):
    def __init__(self, identifier: str, positions):
        super().__init__(identifier, positions)

    def move(self, game_board):
        pass


class Player(Agent):
    def __init__(self, identifier, positions):
        super().__init__(identifier, positions)

    def move(self, game_board):
        keys = pygame.key.get_pressed()
        head = self._positions[-1]
        if keys[K_w]:
            self._positions.append((head[0], head[1] + 1))
            self._positions.pop(0)
        elif keys[K_a]:
            self._positions.append((head[0] - 1, head[1]))
            self._positions.pop(0)
        elif keys[K_s]:
            self._positions.append((head[0], head[1] - 1))
            self._positions.pop(0)
        elif keys[K_d]:
            self._positions.append((head[0] + 1, head[1]))
            self._positions.pop(0)


class AI(Agent):
    def __init__(self, identifier, positions):
        super().__init__(identifier, positions)
