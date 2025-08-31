import pygame
import sys,os
import time
import pyglet
import random
from pygame.locals import *

WIDE_SCREEN = 1300
LONG_SCREEN = 900
GRAVITY = 0.5
JUMP_POWER = -10

class Player:
    def __init__(self, screen):
        self.screen = screen
        self.bird = pygame.Rect(550, (LONG_SCREEN // 2) - 25, 50, 50)
        self.velocity_y = 0  # Vertical speed

    def draw(self):
        pygame.draw.rect(self.screen, (255, 255, 0), self.bird)

    def jump(self):
        self.velocity_y = JUMP_POWER  # Takes up impuls

    def gravity(self):
        self.velocity_y += GRAVITY  # Gravity makes faster falling
        self.bird.y += int(self.velocity_y)  # Change position per speed

    def check_position(self):
        return 0 < self.bird.y < 900
    def set_position(self):
        self.bird.y = 550