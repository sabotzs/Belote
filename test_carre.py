import unittest
from carre import Carre
from announcement import Announcement
from card import Card

class TestCarre(unittest.TestCase):
    def test_get_carres_return_empty_list_when_no_carre(self):
        ann = Announcement()
        hand = [
            [
                Card('7','c'), Card('8','c'), Card('9','c'),
                Card('Q','c'), Card('K','c'), Card('A','c')
            ],[],[],[]
        ]
        result = ann.get_carres(hand)
        self.assertEqual(result,[])

    def test_get_carres(self):
        ann = Announcement()
        hand = [
            [Card('Q','c')], [Card('Q','s')], [Card('Q','d')], [Card('Q','h')]
        ]
        result = ann.get_carres(hand)
        expected = [Carre([ Card('Q','c'), Card('Q','s'), Card('Q','d'), Card('Q','h') ]) ]
        self.assertEqual(result,expected)

    def test_carre(self):
        car1 = Carre([Card('7','s')])
        l1 = [car1]
        car2 = Carre([Card('7','s')])
        l2 = [car2]
        self.assertEqual(l1,l2)

    def test_two_cares_in_one_hand(self):
        ann = Announcement()
        hand = [
            [Card('10','c'),Card('Q','c')], [Card('10','s'),Card('Q','s')], [Card('10','d'),Card('Q','d')], [Card('10','h'),Card('Q','h')]
            ]
        result = ann.get_carres(hand)
        expected = [
            Carre([Card('10','c'), Card('10','s'), Card('10','d'), Card('10','h')]),
            Carre([Card('Q','c'), Card('Q','s'), Card('Q','d'), Card('Q','h')])

        ]
        self.assertEqual(result,expected)

if __name__ == '__main__':
    unittest.main()
