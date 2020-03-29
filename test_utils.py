import unittest
from utils import sort_part_by_face, sort_hand_by_face, sort_hand, get_face_index
from card import Card

class TestUtils(unittest.TestCase):
    def test_sort_hand(self):
        cards = [
        Card('9','s'),
        Card('10','h'),
        Card('Q','c'),
        Card('10','c'),
        Card('K','d'),
        Card('K','c'),
        Card('A','s'),
        Card('J','d')
        ]
        self.assertEqual(sort_hand(cards),
            [Card('10','c'),
            Card('Q','c'),
            Card('K','c'),
            Card('J','d'),
            Card('K','d'),
            Card('10','h'),
            Card('9','s'),
            Card('A','s')])

if __name__ == '__main__':
    unittest.main()