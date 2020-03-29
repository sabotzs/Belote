import unittest
from card import Card

class TestCard(unittest.TestCase):
<<<<<<< HEAD
    def test_initialising_with_invalid_face_raises_value_error(self):
        with self.assertRaises(ValueError):
            Card('5', 's')

    def test_initialising_with_invalid_suit_raises_value_error(self):
        with self.assertRaises(ValueError):
            Card('8', 'f')

    def test_string_representation_is_the_expected_one(self):
        card1 = Card('7', 's')
        card2 = Card('Q', 'h')

        self.assertEqual(str(card1), '7s')
        self.assertEqual(str(card2), 'Qh')

    def test_passes_if_same_cards_are_compared_equal(self):
        card1 = Card('7', 's')
        card2 = Card('7', 's')

        self.assertTrue(card1 == card2, 'Cards are not the same.')

    def test_passes_if_first_card_is_compared_greater_than_the_second(self):
        card1 = Card('8', 'd')
        card2 = Card('J', 's')

        self.assertTrue(card2 > card1, 'First card is not greater than the second.')


if __name__ == '__main__':
    unittest.main()
=======
	def test_initialising_with_invalid_face_raises_value_error(self):
		with self.assertRaises(ValueError):
			Card('5', 's')

	def test_initialising_with_invalid_suit_raises_value_error(self):
		with self.assertRaises(ValueError):
			Card('8', 'f')

	def test_string_representation_is_the_expected_one(self):
		card1 = Card('7', 's')
		card2 = Card('Q', 'h')

		self.assertEqual(str(card1), '7s')
		self.assertEqual(str(card2), 'Qh')

	def test_passes_if_same_cards_are_compared_equal(self):
		card1 = Card('7', 's')
		card2 = Card('7', 's')

		self.assertTrue(card1 == card2, 'Cards are not the same.')

	def test_passes_if_first_card_is_compared_greater_than_the_second(self):
		card1 = Card('8', 'd')
		card2 = Card('J', 's')

		self.assertTrue(card1 > card2, 'First card is not greater than the second.')


if __name__ == '__main__':
	unittest.main()
>>>>>>> master
