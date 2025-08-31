import pygame
import sys,os
import time
import pyglet
import random
from pygame.locals import *
import player
import config

WIDE_SCREEN = 1300
LONG_SCREEN = 900
GAP_HEIGHT = 200
TEMPO = 5
OBSTACLE_DISTANCE = 600



class Obstacle:
    def __init__(self, screen):
        self.screen = screen
        self.height_top = random.randint(150, 500)
        self.speed = 200  # PIXELS per second
        self.last_speedup = pygame.time.get_ticks()
        self.obstacles = []

    def create_obstacle(self):
        self.obstacle_top = pygame.Rect(1300, 0 , 50, self.height_top)
        self.start_bottom = self.height_top + GAP_HEIGHT
        self.height_bottom = LONG_SCREEN - self.start_bottom
        self.obstacle_bottom = pygame.Rect(1300, self.start_bottom, 50, self.height_bottom)
        self.passed = False
        self.obstacles.append(self)

    def reset_obstacles(self):
        self.obstacles = []
        
        
    def move_obstacle(self,dt):
        for obstacle in self.obstacles:
            obstacle.obstacle_top.x -= self.speed * dt
            obstacle.obstacle_bottom.x -= self.speed * dt
            if pygame.time.get_ticks() - self.last_speedup > 5000:
                self.speed += 2
                self.last_speedup = pygame.time.get_ticks()
      

    def draw(self):
        for obstacle in self.obstacles:
            pygame.draw.rect(self.screen, (0, 255, 0), obstacle.obstacle_top)
            pygame.draw.rect(self.screen, (0, 255, 0),obstacle.obstacle_bottom)

    def new_obstacle(self):
        if self.obstacles[-1].obstacle_bottom.x < (player.WIDE_SCREEN - OBSTACLE_DISTANCE):
            new_obstacle = Obstacle(self.screen)
            new_obstacle.create_obstacle()
            self.obstacles.append(new_obstacle)

    def check_collision(self,player):
        self.player = player
        result = False
        for obstacle in self.obstacles:
            if self.player.bird.colliderect(obstacle.obstacle_top) or self.player.bird.colliderect(
                    obstacle.obstacle_bottom):
                return True
            if not obstacle.passed and obstacle.obstacle_top.x + obstacle.obstacle_top.width < self.player.bird.x:
                obstacle.passed = True
                result = "passed"
        return result

  