import unittest
from announcement import Announcement
from card import Card
from consecutive import Consecutive

class TestAnnouncement(unittest.TestCase):
	def test_passes_with_two_tierces_from_same_suit(self):
		ann = Announcement()
		hand = [
			[
				Card('7','c'), Card('8','c'), Card('9','c'),
				Card('Q','c'), Card('K','c'), Card('A','c')
			]
		]

		result = ann.get_consecutive(hand)

		self.assertEqual(result, [
			Consecutive([Card('7','c'), Card('8','c'), Card('9','c')]),
			Consecutive([Card('Q','c'), Card('K','c'), Card('A','c')])
		])


	def test_passes_with_tierce_and_quinte(self):
		ann = Announcement()
		hand = [
			[Card('7','c'), Card('8','c'), Card('9','c')],
			[Card('7','s'), Card('8','s'), Card('9','s'), Card('10', 's'), Card('J','s')]
		]

		result = ann.get_consecutive(hand)

		self.assertEqual(result, [
			Consecutive([Card('7','c'), Card('8','c'), Card('9','c')]),
			Consecutive([Card('7','s'), Card('8','s'), Card('9','s'), Card('10', 's'), Card('J','s')])
		])

	def test_are_consecutive(self):
		ann = Announcement()
		card = Card('9', 's')
		card1 = Card('Q', 's')
		card2 = Card('K', 's')

		self.assertTrue(ann.are_consecutive(card1, card2))
		self.assertFalse(ann.are_consecutive(card, card1))

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
