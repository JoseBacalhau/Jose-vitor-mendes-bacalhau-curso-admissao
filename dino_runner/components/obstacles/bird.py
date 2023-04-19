import random
from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle
from random import choice

class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = choice((250, 300, 330))
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0