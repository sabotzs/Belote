import unittest
from game import Game
from player import Player
from team import Team
from belote import Belote
from deck import Deck
from dealer import Dealer
from announcement import Announcement
import random
from consecutive import Consecutive

class TestGame(unittest.TestCase):
    def test_create_game_with_no_team(self):
        exc = None
        t = Team("Cats",Player("Misho"),Player("Pesho"))
        try :
            Game(Player("Ivan"),t)
        except TypeError as error:
            exc = error
        self.assertIsNotNone(exc)

    def test_create_game_with_teams_with_common_player(self):
        exc = None
        t1 = Team("Cats",Player("Misho"),Player("Pesho"))
        t2 = Team("Dogs",Player("Misho"),Player("Ivanka"))
        try:
            g = Game(t1,t2)
        except TypeError as error:
            exc = error
        self.assertIsNotNone(exc)

    def test_spin_players(self):
        exc = None
        t1 = Team("Cats",Player("Maria"),Player("Pesho"))
        t2 = Team("Dogs",Player("Misho"),Player("Ivanka"))
        try:
            g = Game(t1,t2)
        except TypeError as error:
            exc = error
        first_order = g.print_table_players()
        g.spin_players()
        second_order = g.print_table_players()
        self.assertNotEqual(first_order,second_order)

    



if __name__ == '__main__':
    unittest.main()