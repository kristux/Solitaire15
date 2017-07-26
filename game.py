from collections import defaultdict

from deck import Deck, Suit
from player import Player


class Game(object):
    def __init__(self, deck, board_size=16):
        self._board_size = board_size
        self._deck = deck
        self._did_win = False
        self._board = self._deck.pull(self._board_size)

    def simulate(self, player):
        board = self._board
        while True:
            cards = player.pick(board[:])
            if not cards:
                break
            for card in cards:
                board.remove(card)
            cards_to_pull = self._deck.pull(self._board_size - len(board))
            if not cards_to_pull:
                self._did_win = True
                break
            board.extend(cards_to_pull)

    def did_win(self):
        return self._did_win


def print_board(board):
    lines = defaultdict(list)
    for idx, card in enumerate(board):
        lines[idx // 4].append(card)
    for cards in lines.values():
        print("\t".join(card_to_string(card) for card in cards))

def card_to_string(card):
    suit, rank = card
    suit_name = {Suit.HEART: "H", Suit.SPADE: "S", Suit.DIAMOND: "D", Suit.CLUB: "C"}[suit]
    return "%s%s" % (suit_name, rank)


