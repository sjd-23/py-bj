class Player:
    def __init__(self):
        self.hand = []

    def calculate_hand_value(self) -> int:
        hand_value = 0
        for card in self.hand:
            if card.id[1] != 'a':
                hand_value += card.value
                continue
            if card.id[1] == 'a' and hand_value + 11 > 21:
                hand_value += 1
                continue
            elif card.id[1] == 'a' and hand_value + 11 <= 21:
                hand_value += 11
                continue
        return hand_value