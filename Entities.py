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
        if game_board[new_head[0]][new_head[1]] in ['1', '2'] and new_head != self._positions[0]:
            return 'lose' + self._identifier
        return ''


class Player(Agent):
    def __init__(self, identifier, positions):
        super().__init__(identifier, positions)

    def move(self, game_board) -> str:
        return super().move(game_board)

    def update_control(self, key):
        if self._direction in ['left', 'right']:
            if key == K_w:
                self._direction = 'up'
            elif key == K_s:
                self._direction = 'down'
        else:
            if key == K_a:
                self._direction = 'left'
            elif key == K_d:
                self._direction = 'right'


class AI(Agent):
    def __init__(self, identifier, positions):
        super().__init__(identifier, positions)


