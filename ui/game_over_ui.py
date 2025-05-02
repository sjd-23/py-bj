import pygame
from pygame import SRCALPHA


class GameOverUI:
    def __init__(self, player, dealer, font):
        self.player = player
        self.dealer = dealer
        self.font = font

        self.hidden = True
        self.player_won = True
        self.push = False

        self.again_area = pygame.Rect(1030, 110, 185, 50)
        self.again_surface = pygame.Surface((self.again_area.w, self.again_area.h), SRCALPHA)
        self.again_surface.fill((15, 15, 15, 100))

        self.quit_area = pygame.Rect(1030, 172, 185, 50)
        self.quit_surface = pygame.Surface((self.quit_area.w, self.quit_area.h), SRCALPHA)
        self.quit_surface.fill((15, 15, 15, 100))

        self.again_color = "gray"
        self.quit_color = "gray"

    def update(self):
        pass

    def draw(self, screen):
        if not self.hidden:
            self._render_title(screen)

            screen.blit(self.again_surface, self.again_area)
            screen.blit(self.quit_surface, self. quit_area)
            again_string = "Play again?"
            again_text = self.font.render(again_string, True, self.again_color)
            screen.blit(again_text, (self.again_area.x + 7, self.again_area.y + 15))
            quit_string = "Quit!"
            quit_text = self.font.render(quit_string, True, self.quit_color)
            screen.blit(quit_text, (self.quit_area.x + 60, self.quit_area.y + 15))

    def _render_title(self, screen):
        title_string = "Game Over"
        title_text = self.font.render(title_string, True, "white")
        screen.blit(title_text, (1030, 25))

        if self.push:
            result_string = "PUSH"
            result_color = "yellow"
            result_location = (1085, 65)
        elif self.player_won:
            result_string = "WIN"
            result_color = "green"
            result_location = (1095, 65)
        else:
            result_string = "LOSS"
            result_color = "red"
            result_location = (1083, 65)

        result_text = self.font.render(result_string, True, result_color)
        screen.blit(result_text, result_location)
