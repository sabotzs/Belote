from utils import sort_hand
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.announcements = []
        self.points = 0

    def __eq__(self,other):
        return self.name == other.name

    def get_cards(self, cards):
        if len(self.hand) == 8:
            self.hand = []

        for card in cards:
            self.hand.append(card)

    def announce(self):
        pass
