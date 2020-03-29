import unittest
from announcement import Announcement
from card import Card
from consecutive import Consecutive

class TestAnnouncement(unittest.TestCase):
    def test_passes_with_two_tierces_from_same_suit(self):
        ann = Announcement()
        hand = [[Card('7','c'), Card('8','c'), Card('9','c'),
        Card('Q','c'), Card('K','c'), Card('A','c')]]
        result = ann.get_consecutive(hand)
        self.assertEqual(result,[Consecutive([Card('7','c'), Card('8','c'), Card('9','c')]),
            Consecutive([Card('Q','c'), Card('K','c'), Card('A','c')])])

    def test_passes_with_tierces_and_quinte(self):
        ann = Announcement()
        hand = [
        
        ]



if __name__ == "__main__":
    unittest.main()