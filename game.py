import pygame
import sys,os
import time
import pyglet
import random

import scoreboard
from pygame.locals import *
import player
import config
import obstacle

clock = pygame.time.Clock()
dt = clock.tick(60) / 1000

class Game:
  
    def __init__(self,screen):
        self.obstacle = obstacle.Obstacle(config.SCREEN)
        self.scoreboard = scoreboard.Scoreboard(config.SCREEN)
        self.game_started = False
        self.screen = screen
        self.player = player.Player(config.SCREEN)

    def initizal_game(self):
        self.obstacle.reset_obstacles()
        self.scoreboard.reset_score()
        self.obstacle.create_obstacle()
        self.obstacle.draw()
        self.player.set_position()
        self.player.jump()




        
        
                
    def start_game(self):
        score = 0
        self.obstacle.new_obstacle()
        self.obstacle.move_obstacle(dt)
        self.player.gravity()
        self.update_screen()
        self.running = True

        collision_result = self.obstacle.check_collision(self.player)
        bird_position = self.player.check_position()


        if collision_result is True or bird_position is False:
            self.running = False
            score = self.scoreboard.score
        elif collision_result == "passed":
            self.scoreboard.update_score()


        return self.running,score
        

      

    def update_screen(self):
        self.screen.fill((0, 0, 0))  # Clear Screen
        self.scoreboard.draw_score()
        self.player.draw()  # Drawing a player
        self.obstacle.draw()  # Drawing obstacles

        pygame.display.flip()

    def end_game(self):
        self.screen.fill((0, 0, 0))
        self.scoreboard.show_score()

    
       
       
        

        
        