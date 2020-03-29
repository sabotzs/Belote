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


if __name__ == '__main__':
	unittest.main()
