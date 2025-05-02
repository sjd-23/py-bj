import os
import pygame
from entities.entity import Entity

class Card(Entity):
    def __init__(self, card_id):
        super().__init__(0, 0, 110, 160)
        self.id = card_id

        # Image loading
        self.sprite_map = {
            "h2": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_2.png")),
            "h3": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_3.png")),
            "h4": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_4.png")),
            "h5": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_5.png")),
            "h6": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_6.png")),
            "h7": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_7.png")),
            "h8": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_8.png")),
            "h9": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_9.png")),
            "h0": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_10.png")),
            "hj": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_j.png")),
            "hq": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_q.png")),
            "hk": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_k.png")),
            "ha": pygame.image.load(os.path.join("assets", "sprites", "cards", "h_a.png")),
            "s2": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_2.png")),
            "s3": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_3.png")),
            "s4": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_4.png")),
            "s5": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_5.png")),
            "s6": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_6.png")),
            "s7": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_7.png")),
            "s8": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_8.png")),
            "s9": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_9.png")),
            "s0": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_10.png")),
            "sj": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_j.png")),
            "sq": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_q.png")),
            "sk": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_k.png")),
            "sa": pygame.image.load(os.path.join("assets", "sprites", "cards", "s_a.png")),
            "d2": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_2.png")),
            "d3": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_3.png")),
            "d4": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_4.png")),
            "d5": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_5.png")),
            "d6": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_6.png")),
            "d7": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_7.png")),
            "d8": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_8.png")),
            "d9": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_9.png")),
            "d0": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_10.png")),
            "dj": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_j.png")),
            "dq": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_q.png")),
            "dk": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_k.png")),
            "da": pygame.image.load(os.path.join("assets", "sprites", "cards", "d_a.png")),
            "c2": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_2.png")),
            "c3": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_3.png")),
            "c4": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_4.png")),
            "c5": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_5.png")),
            "c6": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_6.png")),
            "c7": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_7.png")),
            "c8": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_8.png")),
            "c9": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_9.png")),
            "c0": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_10.png")),
            "cj": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_j.png")),
            "cq": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_q.png")),
            "ck": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_k.png")),
            "ca": pygame.image.load(os.path.join("assets", "sprites", "cards", "c_a.png"))
        }
        self.image = pygame.transform.scale(self.sprite_map[self.id], (self.rect.w, self.rect.h))

        self.value_map = {
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "0": 10,
            "j": 10,
            "q": 10,
            "k": 10,
            "a": 0
        }
        self.value = self.value_map[self.id[1]]
        self.highlight = False

    def update(self, dt):
        if self.highlight:
            self.rect.w = 112
            self.rect.h = 162
            self.image = pygame.transform.scale(self.sprite_map[self.id], (self.rect.w, self.rect.h))
        else:
            self.rect.w = 110
            self.rect.h = 160
            self.image = pygame.transform.scale(self.sprite_map[self.id], (self.rect.w, self.rect.h))

    def draw(self, screen, x, y):
        self.rect.x = x
        self.rect.y = y
        screen.blit(self.image, self.rect)