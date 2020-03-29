import unittest
from announcement import Announcement
from card import Card
from consecutive import Consecutive
from carre import Carre

class TestAnnouncement(unittest.TestCase):
    def test_get_consecutive_passes_with_two_tierces_from_same_suit(self):
        ann = Announcement()
        hand = [
            [
                Card('7','c'), Card('8','c'), Card('9','c'),
                Card('Q','c'), Card('K','c'), Card('A','c')
            ]
        ]

        result = ann.get_consecutives(hand)

        self.assertEqual(result, [
            Consecutive([Card('7','c'), Card('8','c'), Card('9','c')]),
            Consecutive([Card('Q','c'), Card('K','c'), Card('A','c')])
        ])

    def test_get_consecutive_passes_with_tierce_and_quinte(self):
        ann = Announcement()
        hand = [
            [Card('7','c'), Card('8','c'), Card('9','c')],
            [Card('7','s'), Card('8','s'), Card('9','s'), Card('10', 's'), Card('J','s')]
        ]
        
        result = ann.get_consecutives(hand)

        self.assertEqual(result, [
            Consecutive([Card('7','c'), Card('8','c'), Card('9','c')]),
            Consecutive([Card('7','s'), Card('8','s'), Card('9','s'), Card('10', 's'), Card('J','s')])
        ])

    def test_check_consecutives_and_carres_passes_with_carre_of_100_points_and_quinte(self):
        ann = Announcement()
        carres = [
            Carre(
                [
                    Card('10', 'c'),
                    Card('10', 'd'),
                    Card('10', 'h'), 
                    Card('10', 's')
                ]
            )
        ]
        consecs = [
            Consecutive(
                [
                    Card('10', 's'),
                    Card('J', 's'),
                    Card('Q', 's'),
                    Card('K', 's'),
                    Card('A', 's')
                ]
            )
        ]

        expected_consecs = consecs
        ann.check_consecutive_and_carres(consecs, carres)

        self.assertEqual(carres, [])
        self.assertEqual(consecs, expected_consecs)

    def test_check_consecutives_and_carres_passes_with_carre_of_jacks_and_quinte(self):
        ann = Announcement()
        carres = [
            Carre(
                [
                    Card('J', 'c'),
                    Card('J', 'd'),
                    Card('J', 'h'), 
                    Card('J', 's')
                ]
            )
        ]
        consecs = [
            Consecutive(
                [
                    Card('10', 's'),
                    Card('J', 's'),
                    Card('Q', 's'),
                    Card('K', 's'),
                    Card('A', 's')
                ]
            )
        ]

        expected_carres = carres
        ann.check_consecutive_and_carres(consecs, carres)

        self.assertEqual(carres, expected_carres)
        self.assertEqual(consecs, [])

    def test_check_consecutives_and_carres_passes_with_carre_and_tierce_with_non_empty_intersection(self):
        ann = Announcement()
        carres = [
            Carre(
                [
                    Card('J', 'c'),
                    Card('J', 'd'),
                    Card('J', 'h'), 
                    Card('J', 's')
                ]
            )
        ]
        consecs = [
            Consecutive(
                [
                    Card('10', 's'),
                    Card('J', 's'),
                    Card('Q', 's')
                ]
            )
        ]

        expected_carres = carres
        ann.check_consecutive_and_carres(consecs, carres)

        self.assertEqual(carres, expected_carres)
        self.assertEqual(consecs, [])

    def test_check_consecutives_and_carres_passes_with_carre_and_tierce_with_empty_intersection(self):
        ann = Announcement()
        carres = [
            Carre(
                [
                    Card('J', 'c'),
                    Card('J', 'd'),
                    Card('J', 'h'), 
                    Card('J', 's')
                ]
            )
        ]
        consecs = [
            Consecutive(
                [
                    Card('7', 's'),
                    Card('8', 's'),
                    Card('9', 's')
                ]
            )
        ]

        expected_carres = carres
        expected_consecs = consecs
        ann.check_consecutive_and_carres(consecs, carres)

        self.assertEqual(carres, expected_carres)
        self.assertEqual(consecs, consecs)

    def test_are_consecutive(self):
        ann = Announcement()
        card = Card('9', 's')
        card1 = Card('Q', 's')
        card2 = Card('K', 's')

        self.assertTrue(ann.are_consecutive(card1, card2))
        self.assertFalse(ann.are_consecutive(card, card1))


if __name__ == '__main__':
    unittest.main()