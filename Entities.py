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


class Agent(Entity):
    def __init__(self, identifier: str, positions):
        super().__init__(identifier, positions)
        self._direction = 'right'

    def move(self, game_board) -> str:
        pass


class Player(Agent):
    def __init__(self, identifier, positions):
        super().__init__(identifier, positions)

    def move(self, game_board):
        keys = pygame.key.get_pressed()
        head = self._positions[-1]

        if self._direction in ['left', 'right']:
            if keys[K_w]:
                self._direction = 'up'
            elif keys[K_s]:
                self._direction = 'down'
        else:
            if keys[K_a]:
                self._direction = 'left'
            elif keys[K_d]:
                self._direction = 'right'

        new_head = head
        match self._direction:
            case 'up':
                new_head = head[0], head[1] + 1
            case 'left':
                new_head = head[0] - 1, head[1]
            case 'down':
                new_head = head[0], head[1] - 1
            case 'right':
                new_head = head[0] + 1, head[1]

        self._positions.append(new_head)
        if game_board[new_head[0]][new_head[1]] != '+':
            self._positions.pop(0)


class AI(Agent):
    def __init__(self, identifier, positions):
        super().__init__(identifier, positions)
