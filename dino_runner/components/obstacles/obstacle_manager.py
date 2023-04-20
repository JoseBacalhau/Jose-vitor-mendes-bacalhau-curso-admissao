import pygame
import random

from dino_runner.components.obstacles.cloud import Cloud
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.power_ups.power_up_manager import PowerUpManager

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        obstacle_type = [
            Cactus(),
            Bird(),
            Cloud()
        ]
    
        if len(self.obstacles) == 0:            
            self.obstacles.append(obstacle_type[random.randint(0,2)])


        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.has_power_up:
                    pygame.time.delay(500)
                    game.playing = False
                    game.death_count += 1
                    game.final_score = game.score
                    self.best_score(game)
                    game.score = 0
                    break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
    
    def best_score(self, game):
        if game.best_score < game.final_score: 
            game.best_score = game.final_score

    def reset_obstacles(self):
        self.obstacles = []
