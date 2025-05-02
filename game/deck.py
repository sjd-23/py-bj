import random
from entities.card import Card

class Deck:
    def __init__(self):
        self.cards = []
        suits = ['h', 's', 'd', 'c']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'j' , 'q', 'k', 'a']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(str(suit + rank)))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_into(self, destination):
        if len(self.cards) != 0:
            card = self.cards.pop()
            print("Dealing: " + str(card.id))
            destination.hand.append(card)

    def reset(self):
        self.cards = []
        suits = ['h', 's', 'd', 'c']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '0', 'j' , 'q', 'k', 'a']

        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(str(suit + rank)))