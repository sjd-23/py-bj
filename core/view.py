import pygame
from ui.hand_ui import HandUI
from ui.dealer_ui import DealerUI
from ui.hit_ui import HitUI
from ui.stay_ui import StayUI
from ui.game_over_ui import GameOverUI
from ui.record_ui import RecordUI

class View:
    def __init__(self, screen, model, font):
        self.screen = screen
        self.model = model
        self.hand_ui = HandUI(self.model.player, font)
        self.dealer_ui = DealerUI(self.model.dealer, font)
        self.hit_ui = HitUI(self.model.player, font)
        self.stay_ui = StayUI(self.model.dealer, font)
        self.game_over_ui = GameOverUI(self.model.player, self.model.dealer, font)
        self.record_ui = RecordUI(font)

    def draw(self):
        pygame.draw.rect(self.screen, (8, 76, 58), (0, 0, 1280, 720))

        self.hand_ui.draw(self.screen)
        self.dealer_ui.draw(self.screen)
        self.hit_ui.draw(self.screen)
        self.stay_ui.draw(self.screen)
        self.game_over_ui.draw(self.screen)
        self.record_ui.draw(self.screen)

        pygame.display.flip()