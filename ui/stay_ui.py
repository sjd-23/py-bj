import pygame
from pygame import SRCALPHA


class StayUI:
    def __init__(self, dealer, font):
        self.dealer = dealer
        self.font = font
        self.area = pygame.Rect(985, 560, 125, 50)
        self.color = "gray"

        self.surface = pygame.Surface((self.area.w, self.area.h), SRCALPHA)
        self.surface.fill((15, 15, 15, 100))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.surface, self.area)

        string = "Stay!"
        text = self.font.render(string, True, self.color)
        screen.blit(text, (self.area.x + 25, self.area.y + 13))