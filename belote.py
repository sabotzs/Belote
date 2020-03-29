class Belote:
    def __init__(self, cards):
        self.cards = cards

    def __int__(self):
        return 20

    def __repr__(self):
        return 'belote'

    def __eq__(self,other):
        return self.cards == other.cards