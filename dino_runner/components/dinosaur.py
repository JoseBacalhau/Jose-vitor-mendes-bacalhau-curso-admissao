import pygame
from pygame.sprite import Sprite

from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING, DEFAULT_TYPE, SHIELD_TYPE, DUCKING_SHIELD, JUMPING_SHIELD, RUNNING_SHIELD, HAMMER_TYPE, DUCKING_HAMMER, JUMPING_HAMMER, RUNNING_HAMMER, GODZILLA_TYPE, JUMPING_GODZILLA, DUCKING_GODZILLA, RUNNING_GODZILLA, DEAD

DUCK_IMG = {DEFAULT_TYPE: DUCKING, SHIELD_TYPE: DUCKING_SHIELD, HAMMER_TYPE: DUCKING_HAMMER, GODZILLA_TYPE: DUCKING_GODZILLA}
JUMP_IMG = {DEFAULT_TYPE: JUMPING, SHIELD_TYPE: JUMPING_SHIELD, HAMMER_TYPE: JUMPING_HAMMER, GODZILLA_TYPE: JUMPING_GODZILLA}
RUN_IMG = {DEFAULT_TYPE: RUNNING, SHIELD_TYPE: RUNNING_SHIELD, HAMMER_TYPE: RUNNING_HAMMER, GODZILLA_TYPE: RUNNING_GODZILLA}

class Dinosaur(Sprite):
    
    def __init__(self):
        self.X_POS =  80
        self.Y_POS = 310
        self.JUMP_VEL = 8.5
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        
        self.jump_vel = self.JUMP_VEL
        self.dino_run = True
        self.dino_jump = False
        self.dino_duck = False
        self.dino_duck_down = False
        self.setup_state()
    
    def setup_state(self):
        self.has_power_up = False
        self.shield = False
        self.hammer = False
        self.godzilla = False
        self.shield_time_up = 0
        
    def update(self, user_input):
        if self.dino_run:
            self.run()
        elif self.dino_jump:
            self.jump()
        elif self.dino_duck:
            self.duck()

        if self.step_index >= 10:
            self.step_index = 0

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_run = False
            self.dino_duck = False
        elif not self.dino_jump:
            self.dino_jump = False
            self.dino_run = True
            self.dino_duck = False
            self.dino_duck_down = False

        if user_input[pygame.K_DOWN]:
            if not self.dino_duck_down:
                self.dino_jump = False
                self.dino_run = False
                self.dino_duck = True
                self.dino_duck_down = True
            else: 
                self.dino_duck_down = False
        
    def run(self):
        self.image = RUN_IMG[self.type][self.step_index // 5] if self.step_index < 5 else RUN_IMG[self.type][1]
        self.dino_rect = self.image.get_rect()
        if self.type == 'godzilla':
            self.dino_rect.x = self.X_POS
            self.dino_rect.y =self. Y_POS - 110
        else:
            self.dino_rect.x = self.X_POS
            self.dino_rect.y =self. Y_POS
        self.step_index += 1

    def jump(self):
        self.image = JUMP_IMG[self.type][self.step_index // 5] if self.step_index < 5 else JUMP_IMG[self.type][1]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.9

        if self.jump_vel < -self.JUMP_VEL:
            if self.type == 'godzilla':
                self.dino_rect.y = self.Y_POS - 110
            else:
                self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def duck(self):
        self.image = DUCK_IMG[self.type][self.step_index // 5] if self.step_index < 5 else DUCK_IMG[self.type][1]
        self.dino_rect = self.image.get_rect()
        if self.dino_duck:
            if self.type == 'godzilla':
                self.dino_rect.y = self.Y_POS - 30
            else:
                self.dino_rect.y = self.Y_POS + 35
            self.dino_rect.x = self.X_POS
            self.jump_vel = self.JUMP_VEL
        self.step_index += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self.image, ( self.dino_rect.x, self.dino_rect.y))