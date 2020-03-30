import unittest
import json
import sys
import os
from card import Card
from team import Team
from player import Player
from pprint import pprint
from json_parse import print_jsonable_round

class TestJson(unittest.TestCase):
    def test_json(self):
        p1 = Player("Maria")
        p2 = Player("Pesho")
        t = Team("Cats", p1, p2)
        cards1 = [
            Card("7","s"), Card("8", "s"),
            Card("9","s"), Card("10","c"), 
            Card("J","d"), Card("Q", "h"), 
            Card("K","h"), Card("A","s")
        ]
        cards2 = [
            Card("7","d"), Card("8","c"),
            Card("9","d"), Card("10","d"),
            Card("J","s"), Card("Q","s"),
            Card("K","d"), Card("A","c")
        ]
        p1.get_cards(cards1)
        p2.get_cards(cards2)

        p5 = Player("ivan")
        p6 = Player("dragan")
        t2 = Team("GG", p5, p6)
        cards3 = [
            Card("7","s"), Card("8", "s"),
            Card("9","s"), Card("10","c"), 
            Card("J","d"), Card("Q", "h"), 
            Card("K","h"), Card("A","s")
        ]
        cards4 = [
            Card("7","d"), Card("8","c"),
            Card("9","d"), Card("10","d"),
            Card("J","s"), Card("Q","s"),
            Card("K","d"), Card("A","c")
        ]
        p5.get_cards(cards3)
        p6.get_cards(cards4)
        contract = "s"
        print(print_jsonable_round(contract,t,t2))


if __name__ == '__main__':
    unittest.main()