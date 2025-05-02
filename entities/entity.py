import pygame

class Entity:
    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.image = None

    def update(self, dt):
        raise NotImplementedError

    def draw(self, screen):
        raise NotImplementedError