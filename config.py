import time

import pygame
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
SCREEN = pygame.display.set_mode((1300, 900))
class Config:

    def create_parameters(self):
        pygame.init()
        self.window = pygame.display.set_mode((1300, 900))
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("FLAPPY BIRD")
        self.wide_screen = 1300
        self.height_screen = 900

        # Title
        self.font = pygame.font.Font(None, 120)
        self.Title = self.font.render("FLAPPY BIRD", True, WHITE)
        self.screen.blit(self.Title, (self.wide_screen // 2 - self.Title.get_width() // 2, 100))


        self.font = pygame.font.Font(None, 36)

        # Text: GRAJ
        game_text_surface = self.font.render("GRAJ", True, GREEN)
        self.game_text_surface1 = game_text_surface.get_rect(center=(self.wide_screen // 2, 300))
        self.screen.blit(game_text_surface, self.game_text_surface1)



        # Text: WYJŚCIE
        exit_text_surface = self.font.render("WYJŚCIE", True, RED)
        self.exit_text_rect1 = exit_text_surface.get_rect(center=(self.wide_screen // 2, 500))
        self.screen.blit(exit_text_surface, self.exit_text_rect1)

        pygame.display.flip()
        
    def create_game(self,name):
        self.screen.fill(BLACK)
        if name == None:
            waiting = self.get_player_name()
            if waiting == False:
                self.game_started = True
        pygame.display.flip()
        return self.player_name,self.game_started

    def new_game(self):
        # Text: GRAJ PONOWNIE
        game_text_surface = self.font.render("GRAJ PONOWNIE", True, GREEN)
        game_text_x = self.wide_screen // 2 - game_text_surface.get_width() // 2
        self.game_text_rect = self.screen.blit(game_text_surface, (game_text_x, 300))

        # Text: LEADBOARD
        leadboard_text_surface = self.font.render("LEADBOARD", True, YELLOW)
        leadboard_text_x = self.wide_screen // 2 - leadboard_text_surface.get_width() // 2
        self.tekst_leadboard_rect = self.screen.blit(leadboard_text_surface, (leadboard_text_x, 400))

        # Text: WYJŚCIE
        exit_text_surface = self.font.render("WYJŚCIE", True, RED)
        exit_text_x = self.wide_screen // 2 - exit_text_surface.get_width() // 2
        self.exit_text_rect = self.screen.blit(exit_text_surface, (exit_text_x, 500))

        pygame.display.flip()

    def get_player_name(self):
        SCREEN_WIDTH, SCREEN_HEIGHT = self.screen.get_size()
        font = pygame.font.SysFont("Arial", 48)
        input_font = pygame.font.SysFont("Arial", 40)

        input_box = pygame.Rect((SCREEN_WIDTH - 400) // 2, 350, 400, 60)
        user_text = ""
        active = False

        button_width, button_height = 250, 70
        button_rect = pygame.Rect((SCREEN_WIDTH - button_width) // 2, 450, button_width, button_height)

        clock = pygame.time.Clock()
        waiting = True

        while waiting:
            self.screen.fill((30, 30, 30))  # clear screen

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = True
                    else:
                        active = False

                    if button_rect.collidepoint(event.pos):
                        if user_text.strip() != "":
                            self.player_name = user_text.strip()
                            waiting = False

                elif event.type == pygame.KEYDOWN and active:
                    if event.key == pygame.K_RETURN:
                        if user_text.strip() != "":
                            self.player_name = user_text.strip()
                            waiting = False
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        if len(user_text) < 20:
                            user_text += event.unicode

            # Drawning input box
            color = (255, 255, 255) if active else (180, 180, 180)
            pygame.draw.rect(self.screen, color, input_box, 2)
            text_surface = input_font.render(user_text or "Wpisz imię...", True, (255, 255, 255))
            self.screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))

            # Drawning a button
            pygame.draw.rect(self.screen, (0, 200, 0), button_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), button_rect, 2)
            btn_text = font.render("Zatwierdź", True, (255, 255, 255))
            btn_rect = btn_text.get_rect(center=button_rect.center)
            self.screen.blit(btn_text, btn_rect)

            pygame.display.flip()
        return waiting





