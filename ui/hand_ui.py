import pygame

class HandUI:
    def __init__(self, player, font):
        self.player = player
        self.font = font
        self.area = pygame.Rect(360, 500, 600, 200)

        self.surface = pygame.Surface((self.area.w, self.area.h),pygame.SRCALPHA)
        self.surface.fill((15, 15, 15, 100))

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.surface, self.area)

        distance = self.area.x + 15
        for card in self.player.hand:
            card.draw(screen, distance, self.area.y + 20)
            distance += 115

        val = self.player.calculate_hand_value()
        color_ranges = [
            ((0, 3), "dark red"),
            ((4, 7), "red"),
            ((8, 11), "dark orange"),
            ((12, 15), "orange"),
            ((16, 20), "green"),
            ((21, 21), "pink"),
            ((22, float('inf')), (230, 3, 255))
        ]

        for (start, end), color in color_ranges:
            if start <= val <= end:
                draw_color = color

        if val >= 22:
            hand_value_string = "Bust with " + str(val) + " :("
        elif val == 21:
            hand_value_string = "Hand value: " + str(val) + "!"
        else:
            hand_value_string = "Hand value: " + str(val)

        text = self.font.render(hand_value_string, True, draw_color)
        screen.blit(text, (self.area.x + 2, self.area.y - 30))