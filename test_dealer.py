import unittest
from player import Player
from card import Card

class TestPlayer(unittest.TestCase):
    def test_(self):
        cards = [Card('10','d'), Card('Q','d'),
                Card('K', 'd'), Card('J', 'd'), 
                Card('A','d')]
        player = Player('Gosho')
        
        player.get_cards(cards)
        
        self.assertEqual(player.hand, cards)

if __name__ == '__main__':
    unittest.main()