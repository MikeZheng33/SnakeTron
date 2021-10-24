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
        head = self._positions[-1]
        new_head = head
        if self._direction == "up":
            new_head = head[0], head[1] + 1
        elif self._direction == "left":
            new_head = head[0] - 1, head[1]
        elif self._direction == "down":
            new_head = head[0], head[1] - 1
        elif self._direction == "right":
            new_head = head[0] + 1, head[1]

        self._positions.append(new_head)
        if new_head[0] < 0 or new_head[0] >= len(game_board) or new_head[1] < 0 or new_head[1] >= len(game_board[0]):
            return 'lose' + self._identifier
        if game_board[new_head[0]][new_head[1]] != '+':
            self._positions.pop(0)
        if game_board[new_head[0]][new_head[1]] == '+':
            return 'apple'
        if game_board[new_head[0]][new_head[1]] in ['1', '2'] and new_head != self._positions[0]:
            return 'lose'


class Player(Agent):
    def __init__(self, identifier, positions):
        super().__init__(identifier, positions)

    def move(self, game_board):
        keys = pygame.key.get_pressed()

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

        return super().move(game_board)


class AI(Agent):
    def __init__(self, identifier, positions):
        super().__init__(identifier, positions)


