from deck import Deck
from game import Game
from player import Player


def run_many(iterations=1000):
    wins = 0
    games = 0

    prefer_fewer_wins = 0
    prefer_more_wins = 0
    print("##### Running %d iteration #####" % (iterations))
    for x in range(10000):
        d1 = Deck()
        d2 = Deck(cards=d1.copy_cards())
        game_more = Game(d1)
        game_more.simulate(Player(prefer_fewer=False))

        game_fewer = Game(d2)
        game_fewer.simulate(Player(prefer_fewer=True))

        if game_more.did_win():
            prefer_more_wins += 1
        if game_fewer.did_win():
            prefer_fewer_wins += 1
        if game_more.did_win() or game_fewer.did_win():
            wins += 1
        games += 1
    print("win ratio:", 100 * wins / games, "either =", wins, "prefer fewer =", prefer_fewer_wins, "prefer more =", prefer_more_wins)
    print(prefer_fewer_wins * 100 / games)
    print(prefer_more_wins * 100 / games)
    print("##### Done #####")


if __name__ == '__main__':
    run_many(iterations=100000)

