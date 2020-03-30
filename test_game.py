import unittest
from game import Game
from player import Player
from team import Team
from belote import Belote
from card import Card
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

    def test_filter_announcements(self):
        t1 = Team("Cats",Player("Maria"),Player("Pesho"))
        t2 = Team("Dogs",Player("Misho"),Player("Ivanka"))
        game = Game(t1, t2)
        ann = [
            Belote([Card('Q','h'), Card('K', 'h')]),
        ]
        game.round_contract = 'c'

        game.filter_announcements(ann)

        self.assertEqual(ann, [])

    def test_delete_consecutive(self):
        t1 = Team("Cats",Player("Maria"),Player("Pesho"))
        t2 = Team("Dogs",Player("Misho"),Player("Ivanka"))
        game = Game(t1, t2)
        ann = [
            Consecutive([Card('Q','h'), Card('K', 'h'), Card('A', 'h')])
        ]
        game.delete_consecutive(ann)

        self.assertEqual(ann, [])

    def test_compare_announcements(self):
        t1 = Team("Cats",Player("Maria"),Player("Pesho"))
        t2 = Team("Dogs",Player("Misho"),Player("Ivanka"))
        game = Game(t1, t2)
        ann1 = [
            Consecutive([Card('Q','h'), Card('K', 'h'), Card('A', 'h')])
        ]
        ann2 = [
            Consecutive([Card('Q','c'), Card('K', 'c'), Card('A', 'c')])
        ]

        game.compare_announcements(ann1, ann2)

        self.assertEqual(ann1, [])
        self.assertEqual(ann2, [])

    def test_get_score_of_round(self):
        t1 = Team("Cats",Player("Maria"),Player("Pesho"))
        t2 = Team("Dogs",Player("Misho"),Player("Ivanka"))
        game = Game(t1, t2)
        ann = [
            Consecutive([Card('Q','h'), Card('K', 'h'), Card('A', 'h')]),
            Belote([Card('Q','h'), Card('K', 'h')])
        ]

        result = game.get_score_of_round(ann)

        self.assertEqual(result, 40)

if __name__ == '__main__':
    unittest.main()