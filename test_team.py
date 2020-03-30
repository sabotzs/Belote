import unittest
from team import Team
from player import Player
from card import Card
from belote import Belote
from consecutive import Consecutive

class TestTeam(unittest.TestCase):
    def test_team_without_players(self):
        exc = None
        try:
            Team("Pesho")
        except TypeError as error:
            exc = error
        self.assertIsNotNone(exc)

    def test_team_with_more_than_two_players(self):
        exc = None
        try:
            Team("Cats",Player("Gosho"),Player("Ivan"),Player("Pesho"))
        except TypeError as error:
            exc = error
        self.assertIsNotNone(exc)

    def test_with_arguments_that_is_not_string(self):
        exc = None
        try:
            Team("Cats","Pesho",12)
        except TypeError as error:
            exc = error
        self.assertIsNotNone(exc)

    def test_with_two_arguments_that_are_strings(self):
        exc = None
        try:
            Team("Cats",Player("Pesho"),Player("Gosho"))
        except TypeError as error:
            exc = error
        self.assertIsNone(exc)

    def test_get_announcements(self):
        p1 = Player("Maria")
        p2 = Player("Pesho")
        t = Team("Cats", p1, p2)
        cards1 = [
            Card("7","s"), Card("8", "s"),
            Card("9","s"), Card("10","c"), 
            Card("J","d"), Card("Q", "h"), 
            Card("K","h"), Card("A","s")
        ]
        cards2 = [
            Card("7","d"), Card("8","c"),
            Card("9","d"), Card("10","d"),
            Card("J","s"), Card("Q","s"),
            Card("K","d"), Card("A","c")
        ]
        p1.get_cards(cards1)
        p2.get_cards(cards2)
        p1.announce()
        p2.announce()

        result = t.get_announcements()

        self.assertEqual(result,
            [
                Belote([Card("Q", "h"), Card("K","h")]),
                Consecutive([Card("7","s"), Card("8", "s"), Card("9","s")])
            ]
        )


if __name__ == '__main__':
    unittest.main()

