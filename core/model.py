from game.deck import Deck
from game.player import Player

class Model:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Player()
        self.deck.shuffle()

    def update(self, dt):
        for card in self.player.hand:
            card.update(dt)

        for card in self.dealer.hand:
            card.update(dt)