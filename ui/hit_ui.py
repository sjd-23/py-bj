import pygame

class HitUI:
    def __init__(self, player, font):
        self.player = player
        self.font = font
        self.area = pygame.Rect(985, 500, 125, 50)
        self.color = "gray"

        self.surface = pygame.Surface((self.area.w, self.area.h), pygame.SRCALPHA)
        self.surface.fill((15, 15, 15, 100))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.surface, self.area)

        string = "Hit!"
        text = self.font.render(string, True, self.color)
        screen.blit(text, (self.area.x + 40, self.area.y + 13))