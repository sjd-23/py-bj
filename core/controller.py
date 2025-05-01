import pygame

class Controller:
    def __init__(self):
        self.game_running = True

    def update(self):
        self.detect_input()

    def detect_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_running = False
                return
            elif event.type == pygame.KEYDOWN:
                self.handle_key_down(event.key)

    def handle_key_down(self, key):
        pass