import os
import random
from collections import Counter

import pygame
from pygame.locals import *
import pickle


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
            return 'lose' + self._identifier
        return ''


class Player(Agent):
    def __init__(self, identifier, positions):
        super().__init__(identifier, positions)
        self.__last_moved_direction = 'right'

    def move(self, game_board) -> str:
        self.__last_moved_direction = self._direction
        return super().move(game_board)

    def update_control(self, key):
        if self._direction in ['left', 'right']:
            if key == K_w and self.__last_moved_direction != 'down':
                self._direction = 'up'
            elif key == K_s and self.__last_moved_direction != 'up':
                self._direction = 'down'
        else:
            if key == K_a and self.__last_moved_direction != 'right':
                self._direction = 'left'
            elif key == K_d and self.__last_moved_direction != 'left':
                self._direction = 'right'


class AI(Agent):
    def __init__(self, identifier, positions, alpha=0, discount=0, epsilon=0):
        super().__init__(identifier, positions)
        self.__q_table_file_name = 'moby.by'
        if os.path.exists(self.__q_table_file_name):
            with open(self.__q_table_file_name, 'rb') as file:
                self.__q_table = pickle.load(file)
        else:
            self.__q_table = {}
        self.__last_game_board = None
        self.__last_move = ''
        self.__legal_moves = ['right']
        self.__alpha = alpha
        self.__discount = discount
        self.__epsilon = epsilon

    def move(self, game_board):
        game_board = tuple(tuple(row) for row in game_board)
        if self._direction in ['left', 'right']:
            self.__legal_moves = ['up', 'down']
        else:
            self.__legal_moves = ['left', 'right']

        if self.__last_game_board is not None:
            if self.__last_game_board not in self.__q_table:
                self.__q_table[self.__last_game_board] = Counter()
            if self.__last_move != '':
                self.__q_table[self.__last_game_board][self.__last_move] += \
                    self.__alpha * (self.__reward(game_board)
                                    + self.__discount * self.__value(game_board)
                                    - self.__q_value(self.__last_game_board, self.__last_move))

        if random.random() < self.__epsilon:
            move = random.choice(self.__legal_moves)
        else:
            max_value = self.__value(game_board)
            move = random.choice([a for a in self.__legal_moves if self.__q_value(game_board, a) == max_value])

        self.__last_game_board = game_board
        self.__last_move = move

        self._direction = move

        self.__write_q_table_file()

        return super(AI, self).move(game_board)

    def __reward(self, game_board):
        my_pieces = 0
        enemy_pieces = 0
        for row in game_board:
            for x in row:
                if x == self._identifier:
                    my_pieces += 1
                elif x not in [' ', '+']:
                    enemy_pieces += 1
        return my_pieces - enemy_pieces

    def __value(self, state):
        return max(self.__q_value(state, action) for action in self.__legal_moves)

    def __q_value(self, state, action):
        return self.__q_table.get(state, Counter())[action]

    def __write_q_table_file(self):
        with open(self.__q_table_file_name, 'wb') as file:
            pickle.dump(self.__q_table, file)
