import pygame

class DealerUI:
    def __init__(self, dealer, font):
        self.dealer = dealer
        self.font = font
        self.area = pygame.Rect(360, 25, 600, 200)

        self.surface = pygame.Surface((self.area.w, self.area.h), pygame.SRCALPHA)
        self.surface.fill((15, 15, 15, 100))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.surface, self.area)

        distance = self.area.x + 15
        for card in self.dealer.hand:
            card.draw(screen, distance, self.area.y + 20)
            distance += 115

        val = self.dealer.calculate_hand_value()
        color_ranges = [
            ((0, 3), "dark red"),
            ((4, 7), "red"),
            ((8, 11), "dark orange"),
            ((12, 15), "orange"),
            ((16, 20), "green"),
            ((21, 21), (247, 179, 197)),
            ((22, float('inf')), (255, 116, 145))
        ]

        for (start, end), color in color_ranges:
            if start <= val <= end:
                draw_color = color

        if val >= 22:
            hand_value_string = "Bust!"
        elif val == 21:
            hand_value_string = "Blackjack!"
        else:
            hand_value_string = "Dealer's value: " + str(val)

        text = self.font.render(hand_value_string, True, draw_color)
        screen.blit(text, (self.area.x + 2, self.area.y + self.area.h + 10))