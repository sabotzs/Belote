import unittest
from player import Player
from card import Card
from belote import Belote
from consecutive import Consecutive

class TestPlayer(unittest.TestCase):
    def test_get_cards_add_a_list_of_cards_to_the_players_hand(self):
        cards = [
            Card('10','d'), Card('Q','d'),
            Card('K', 'd'), Card('J', 'd'), 
            Card('A','d')
        ]
        player = Player('Gosho')        
        player.get_cards(cards)

        self.assertEqual(player.hand, cards)

    def test_announce_sets_players_announcements_and_point(self):
        cards = [
            Card('9', 'c'), Card('10', 'd'), 
            Card('Q', 'd'), Card('K', 'd'), 
            Card('J', 'd'), Card('A', 'd'),
            Card('K', 'h'), Card('A', 's')
        ]
        player = Player('Gosho')
        player.get_cards(cards)

        player.announce()

        self.assertEqual(player.announcements, 
            [
                Belote([Card('Q', 'd'), Card('K', 'd')]),
                Consecutive(
                    [
                        Card('10', 'd'), Card('J', 'd'),
                        Card('Q', 'd'), Card('K', 'd'), 
                        Card('A', 'd'),
                    ]
                )
            ]
        )
        self.assertEqual(player.points, 120)


if __name__ == '__main__':
    unittest.main()