import random
from enum import Enum


class Suit(Enum):
    HEART = 1
    SPADE = 2
    DIAMOND = 3
    CLUB = 4


class Deck(object):
    def __init__(self, cards=None):
        if cards is not None:
            self._cards = cards
        else:
            self._cards = []
            for suit in Suit:
                for rank in range(1, 14):
                    self._cards.append((suit, rank))
            random.shuffle(self._cards)

    def pull(self, amount):
        if not self._cards:
            return None
        cards_to_return = self._cards[:amount]
        self._cards = self._cards[amount:]
        return cards_to_return

    def copy(self):
        return Deck(self._cards[:])

