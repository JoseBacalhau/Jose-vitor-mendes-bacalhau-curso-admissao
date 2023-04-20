import random
from random import choice

from dino_runner.utils.constants import CLOUD
from dino_runner.components.obstacles.obstacle import Obstacle

class Cloud(Obstacle):
    def __init__(self):
        super().__init__(CLOUD, 0)
        self.rect.y = 50
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 10:
            self.step_index = 0