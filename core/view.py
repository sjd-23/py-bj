import pygame

class View:
    def __init__(self, screen):
        self.screen = screen

    def draw(self):
        pygame.display.flip()