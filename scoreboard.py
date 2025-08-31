import obstacle
import pygame
import sys,os
import time
import pyglet
import random
from pygame.locals import *
import player
import config
import json



class Scoreboard:
    def __init__(self,screen):
        self.screen = screen
        self.score = 0
    def draw_score(self):
        font = pygame.font.SysFont(None, 48)
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (obstacle.WIDE_SCREEN - 200, 20))

    def update_score(self):
        self.score += 1
    def reset_score(self):
        self.score = 0

    def show_score(self):
        font = pygame.font.SysFont("Comic Sans MS", 60)  # Rozmiar 60, domyślna czcionka
        text = font.render(f"Twój wynik to:  {self.score}", True, (255, 255, 255))  # Biały kolor
        text_rect = text.get_rect(center=(obstacle.WIDE_SCREEN // 2, 200))
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def add_score(self,score,best_score,player_name):
        if score > best_score:
            best_score = score
            self.load_leadboard()
            self.leadboard[player_name] = score
            self.save_scores()

        return best_score

    def load_leadboard(self):
        if os.path.exists("scores.json"):
            try:
                with open("scores.json", 'r') as f:
                    self.leadboard = json.load(f)
            except (json.JSONDecodeError, ValueError):
                self.leadboard = {}
        else:
            self.leadboard = {}

    def get_top_scores(self, limit=10):
        # Return TOP 10 scores
        return sorted(self.leadboard.items(), key=lambda x: x[1], reverse=True)[:limit]
    def save_scores(self):
        # Save scores to JSON
        with open("scores.json", 'w') as f:
            json.dump(self.leadboard, f)


    def show_leadboard(self):
        self.load_leadboard()
        font = pygame.font.SysFont("Comic Sans MS", 34)
        self.screen.fill((0, 0, 0))
        title = font.render("LEADERBOARD", True, (255, 255, 255))
        self.screen.blit(title, (self.screen.get_width() // 2 - title.get_width() // 2, 50))
        top_scores = self.get_top_scores()
        y = 150
        for idx, (name, score) in enumerate(top_scores, start=1):
            text = font.render(f"{idx}. {name}: {score}", True, (255, 255, 255))
            self.screen.blit(text, (self.screen.get_width() // 2 - text.get_width() // 2, y))
            y += 50
        back_text = font.render("POWRÓT", True, (255, 0, 0))
        self.back_rect = back_text.get_rect(center=(self.screen.get_width() // 2, y + 100))
        self.screen.blit(back_text, self.back_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.back_rect.collidepoint(event.pos):
                        waiting = False
                        return "back"


