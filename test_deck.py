import unittest
from deck import Deck, Card

class TestDeck(unittest.TestCase):
    def test_two_decks_are_compared_equal_if_the_order_of_the_cards_in_them_is_the_same(self):
        deck1 = Deck()
        deck2 = Deck()

        self.assertTrue(deck1 == deck2, 'Decks don\'t have the same order.')

    def test_len_returns_the_number_of_cards_in_the_deck(self):
        deck = Deck()

        length = len(deck)

        self.assertEqual(length, 32)

    def test_getitem_returns_the_card_with_give_index(self):
        deck = Deck()

        card = deck[5]

        self.assertEqual(card, deck.cards[5])

    def test_setitem_changes_the_card_at_the_given_index_with_the_given_one(self):
        deck = Deck()

        deck[0] = Card('A', 's')

        self.assertEqual(deck.cards[0], Card('A', 's'))

if __name__ == '__main__':
    unittest.main()