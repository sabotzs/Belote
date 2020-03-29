import unittest
from dealer import Dealer, Deck

class TestDealing(unittest.TestCase):
    def test_passes_if_shuffle_changes_the_deck(self):
        deck1 = Deck()
        
        Dealer.shuffle_deck(deck1)

        self.assertNotEqual(deck1, Deck())

    def test_first_dealing_first_deals_three_and_then_two_cards_to_each_hand(self):
        deck = Deck()

        result = Dealer.first(deck)

        self.assertEqual(result[0], [deck[0], deck[1], deck[2], deck[12], deck[13]])
        self.assertEqual(result[1], [deck[3], deck[4], deck[5], deck[14], deck[15]])
        self.assertEqual(result[2], [deck[6], deck[7], deck[8], deck[16], deck[17]])
        self.assertEqual(result[3], [deck[9], deck[10], deck[11], deck[18], deck[19]])

    def test_second_dealing_gives_three_cards_to_each_hand(self):
        deck = Deck()

        result = Dealer.second(deck)

        self.assertEqual(result[0], [deck[20], deck[21], deck[22]])
        self.assertEqual(result[1], [deck[23], deck[24], deck[25]])
        self.assertEqual(result[2], [deck[26], deck[27], deck[28]])
        self.assertEqual(result[3], [deck[29], deck[30], deck[31]])

if __name__ == '__main__':
    unittest.main()