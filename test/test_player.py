from unittest import TestCase

from deck import Suit
from player import Player, get_matches, Matches


class TestPlayer(TestCase):
    def test_empty_list_returns_empty_list(self):
        player = Player()
        self.assertEqual(player.pick([]), [])

    def test_8_and_7(self):
        player = Player()
        cards = [(Suit.DIAMOND, 7), (Suit.HEART, 8), (Suit.HEART, 7), ]
        self.assertEqual(((Suit.HEART, 8), (Suit.HEART, 7)), player.pick(cards))

    def test_different_sort(self):
        player = Player()
        cards = [(Suit.DIAMOND, 7), (Suit.HEART, 8)]
        self.assertEqual([], player.pick(cards))

    def test_prefer_fewer(self):
        cards = shortnames_to_cards("h7", "h8", "h6", "h2")
        self.assertEqual(Player(prefer_fewer=True).pick(cards), shortnames_to_cards("h7", "h8"))
        self.assertEqual(Player(prefer_fewer=False).pick(cards), shortnames_to_cards("h7", "h6", "h2"))


class TestGetMatches(TestCase):
    def test_(self):
        self.assertEqual(get_matches([]), [])
        self.assertMatches(["h7", "h8"], [["h7", "h8"]])
        self.assertMatches(["h7", "h9"], [])
        self.assertMatches(["h4", "h11"], [])
        self.assertMatches(["h11", "h12", "h13"], [["h11", "h12", "h13"]])
        self.assertMatches(["h7", "s8"], [])
        self.assertMatches(["h1", "h6", "h9"], [["h6", "h9"]])
        self.assertMatches(["h1", "h5", "h9"], [["h1", "h5", "h9"]])
        self.assertMatches(["h10", "s10", "d10", "c10"], [["h10", "s10", "d10", "c10"]])
        self.assertMatches(["h9", "h5", "h1", "h6"], [["h9", "h6"], ["h9", "h5", "h1"]])
        self.assertMatches(["h7", "h8", "h11"], [["h7", "h8"]])

    def assertMatches(self, cards, matches):
        self.assertCountEqual(get_matches(shortnames_to_cards(*cards)), [shortnames_to_cards(*m) for m in matches])

def shortnames_to_cards(*shortnames):
    return tuple(shortname_to_card(s) for s in shortnames)

def shortname_to_card(shortname):
    suit = {"h": Suit.HEART, "s": Suit.SPADE, "d": Suit.DIAMOND, "c": Suit.CLUB}[shortname[0].lower()]
    return (suit, int(shortname[1:]))

