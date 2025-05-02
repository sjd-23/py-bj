import pygame

class RecordUI:
    def __init__(self, font):
        self.font = font
        self.win_count = 0
        self.push_count = 0
        self.loss_count = 0

    def update(self):
        pass

    def draw(self, screen):
        win_text = self.font.render(str(self.win_count), True, "green")
        push_text = self.font.render(str(self.push_count), True, "yellow")
        loss_text = self.font.render(str(self.loss_count), True, "red")
        screen.blit(win_text, (10, 10))
        screen.blit(push_text, (10, 50))
        screen.blit(loss_text, (10, 90))