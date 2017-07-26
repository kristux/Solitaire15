from unittest import TestCase

from deck import Deck


class TestDeck(TestCase):
    def setUp(self):
        self._deck = Deck()

    def test_create_deck(self):
        self.assertEqual(self._deck.pull(0), [])

    def test_pull_5_cards(self):
        self.assertEqual(len(self._deck.pull(5)), 5)

    def test_pull_all_the_cards(self):
        self.assertEqual(len(self._deck.pull(52)), 52)

    def test_pulling_more_cards_than_are_in_the_deck(self):
        self._deck.pull(52)
        self.assertEqual(self._deck.pull(52), None)

    def test_can_copy_deck(self):
        d1 = Deck()
        d2 = d1.copy()
        for c1, c2 in zip(d1.pull(52), d2.pull(52)):
            self.assertEqual(c1, c2)

