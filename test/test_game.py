from unittest import TestCase
import mock

from game import Game


class TestGame(TestCase):
    def setUp(self):
        self._deck = mock.Mock()
        self._deck.pull.side_effect = [[1, 2, 3]]
        self._game = Game(self._deck, 3)
        self._player = mock.Mock()

    def test_game_simple(self):
        # self._deck.pull.return_value = [1, 2, 3]
        self._player.pick.return_value = []
        self._simulate()
        self._deck.pull.assert_called_once_with(3)
        self._player.pick.assert_called_once_with([1, 2, 3])

    def test_game_2nd_round(self):
        self._deck.pull.side_effect = [[4]]
        self._player.pick.side_effect = [[3], []]
        self._simulate()
        self.assertEqual(self._deck.pull.call_args_list, [mock.call(3), mock.call(1)])
        self.assertEqual(self._player.pick.call_args_list, [mock.call([1, 2, 3]), mock.call([1, 2, 4])])

    def test_victory_condition(self):
        self._deck.pull.side_effect = [[4], None]
        self._player.pick.side_effect = [[3], [1, 2, 4]]
        self._simulate()
        self.assertEqual(self._deck.pull.call_args_list, [mock.call(3), mock.call(1), mock.call(3)])
        self.assertEqual(self._player.pick.call_args_list, [mock.call([1, 2, 3]), mock.call([1, 2, 4])])

    def _simulate(self):
        self._game.simulate(self._player)

