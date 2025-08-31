import config
import pygame
import sys,os
import time
import pyglet
import random
import game
import obstacle
import player
from pygame.locals import *
import scoreboard
from config import SCREEN


# Creating objects and parameters
settings = config.Config()
settings.create_parameters()
clock = pygame.time.Clock()
game = game.Game(SCREEN)
player = game.player
scoreboard = scoreboard.Scoreboard(SCREEN)
name = None
best_score = 0
game_started = False


# Function which is showing screen after game and manage whats next
def show_end_screen(score,best_score,name):
    global program_running
    global button_clicked
    global game_started
    button_clicked = False
    game.end_game()
    # adding best score to current player and to leadboard
    best_score = scoreboard.add_score(score,best_score,name)
    # Show screen of options what's next
    settings.new_game()

    waiting = True
    # request handling
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_running = False
                waiting = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()

                if settings.game_text_rect.collidepoint(mouse_position):
                    waiting = False
                    game_started = True
                    game.initizal_game()


                elif settings.exit_text_rect.collidepoint(mouse_position):
                    program_running = False
                    waiting = False

                elif settings.tekst_leadboard_rect.collidepoint(mouse_position):
                    result = scoreboard.show_leadboard()
                    if result == "back":
                        waiting = False
                        show_end_screen(score,best_score,name)


    return best_score


program_running = True
button_clicked = False

# Main Loop
while program_running:
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                program_running = False
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN and not button_clicked and game_started == False:
                mouse_position = pygame.mouse.get_pos()
                # Starting a game by click of mouse
                if settings.game_text_surface1.collidepoint(mouse_position):
                    name,game_started = settings.create_game(name)
                    game.initizal_game()
                # Opens settings
                elif settings.exit_text_rect1.collidepoint(mouse_position):
                    running = False
                    program_running = False

            elif event.type == pygame.KEYDOWN:
                # Starting a game by pressing a SPACE
                if event.key == pygame.K_SPACE and game is not None:
                    game_started = True
                    player.jump()
                    game.update_screen()

        # object game used as control of game
        if game_started and game is not None and running is True:
            clock.tick(60)
            running, score = game.start_game()
            # game finished because of out of position or collide
            if running == False:
                # sending best score to end screen to update a leadboard
                best_score = show_end_screen(score,best_score,name)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False




