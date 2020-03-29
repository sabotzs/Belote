import unittest
from utils import sort_part_by_face, sort_hand_by_face, sort_hand
from card import Card

class TestUtils(unittest.TestCase):
    def test_sort_part_by_face_sorts_the_cards_in_part_in_ascending_order(self):
        cards = [
            Card('10', 's'), 
            Card('A', 's'), 
            Card('9', 's'), 
            Card('7', 's')
        ]

        sort_part_by_face(cards)

        self.assertEqual(cards, 
            [
                Card('7', 's'),
                Card('9', 's'), 
                Card('10', 's'), 
                Card('A', 's')
            ]
        )

    def test_sort_hand_sorts_by_suit_and_then_by_face_in_ascending_order(self):
        cards = [
            Card('A', 's'),
            Card('9', 's'),
            Card('10', 'h'),
            Card('Q', 'c'),
            Card('10', 'c'),
            Card('K', 'd'),
            Card('K', 'c'),
            Card('J', 'd')
        ]

        cards = sort_hand(cards)

        self.assertEqual(cards, [
                Card('10', 'c'),
                Card('Q', 'c'),
                Card('K', 'c'),
                Card('J', 'd'),
                Card('K', 'd'),
                Card('10', 'h'),
                Card('9', 's'),
                Card('A', 's')
            ]
        )

if __name__ == '__main__':
    unittest.main()