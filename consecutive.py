class Consecutive:
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        if len(self.cards) == 3:
            return 'tierce'
        if len(self.cards) == 4:
            return 'quarto'
        if len(self.cards) == 5:
            return 'quinte'

    def __int__(self):
        if len(self.cards) == 3:
            return 20
        if len(self.cards) == 4:
            return 50
        if len(self.cards) == 5:
            return 100

    def __eq__(self,other):
        return self.cards == other.cards

    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return str(self.cards)