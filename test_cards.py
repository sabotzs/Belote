import unittest
from cards import Cards
from random import shuffle
from card import Card

class TestCards(unittest.TestCase):
    def test_create_deck(self):
        created_deck = Cards()
        created_deck.show_cards()

    def test_length_of_deck(self):
        created_deck = Cards()
        self.assertEqual(32,len(created_deck.deck))

    def test_shuffle_functionality(self):
        created_deck = Cards()
        first = created_deck.deck
        created_deck.shuffle_cards()
        second = created_deck.deck
        self.assertNotEqual(created_deck,second)



if __name__ == '__main__':
    unittest.main()