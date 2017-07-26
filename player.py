from collections import defaultdict

import itertools


class Player(object):
    def __init__(self, prefer_fewer=False):
        self._prefer_fewer = prefer_fewer

    def pick(self, cards):
        m = Matches(cards)
        tens = m.get_tens()
        if tens:
            return tens[0]
        face_cards = m.get_face_card_matches()
        if face_cards:
            return face_cards[0]
        pips = self._get_pip_matches(m)
        if pips:
            return pips[0]
        return []

    def _get_pip_matches(self, matches):
        return sorted(matches.get_pip_card_matches(), key=lambda x: len(x), reverse=not self._prefer_fewer)


def get_matches(cards):
    return Matches(cards).get()


class Matches(object):
    def __init__(self, cards):
        self._cards_by_suit = defaultdict(list)
        self._tens = []
        for card in cards:
            suit, rank = card
            if rank == 10:
                self._tens.append(card)
            else:
                self._cards_by_suit[suit].append(card)

    def get(self):
        return self.get_pip_card_matches() + self.get_face_card_matches() + self.get_tens()

    def get_tens(self):
        if len(self._tens) == 4:
            return [tuple(self._tens)]
        return []

    def get_pip_card_matches(self):
        matches = []
        for combinator in range(2, 5):
            for eligible_cards in self._iter_suited_pip_cards():
                for combination_cards in itertools.combinations(eligible_cards, combinator):
                    if sum(v for _, v in combination_cards) == 15:
                        matches.append(combination_cards)
        return matches

    def _iter_suited_pip_cards(self):
        for suited_cards in self._cards_by_suit.values():
            yield filter(lambda x: x[1] < 10, suited_cards)

    def get_face_card_matches(self):
        ret = []
        for face_cards in self._iter_suited_face_cards():
            if len(face_cards) == 3:
                ret.append(tuple(face_cards))
        return ret

    def _iter_suited_face_cards(self):
        for cards in self._cards_by_suit.values():
            yield list(filter(lambda x: x[1] > 10, cards))

