from utils import sort_hand
from announcement import Announcement

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.announcements = []
        self.points = 0

    def __eq__(self,other):
        return self.name == other.name

    def get_cards(self, cards):
        self.hand = []

        for card in cards:
            self.hand.append(card)

    def announce(self):
        self.announcements = []
        self.points = 0

        ann = Announcement()
        
        suits = sort_hand(self.hand)
        self.announcements = ann.get_announcements(suits)

        for player_ann in self.announcements:
            self.points += int(player_ann)