class Entity:
    def __init__(self, position: list[int]):
        self.position = position

    def get_position(self):
        pass

    def set_position(self, value):
        self.position = value


class Apple(Entity):
    def __init__(self, position: list[int]):
        super().__init__(self, position)


class Agent(Entity):
    def __init__(self, agent_number: int, position: list[int]):
        super().__init__(position)
        self.agent_number = agent_number

    def get_agent_number(self):
        return self.agent_number

    def set_agent_number(self, agent_number):
        self.agent_number = agent_number

    def move(self, delta_x, delta_y):
        self.position[0] += delta_x
        self.position[1] += delta_y


class Player(Agent):
    def __init__(self, agent_number, position):
        super().__init__(agent_number, position)


class AI(Agent):
    def __init__(self, agent_number, position):
        super().__init__(agent_number, position)