class Consecutive:
    def __init__(self,cards):
        self.cards = cards

	def __eq__(self, other):
		return self.cards == other.cards

	def __gt__(self, other):
		if len(self.cards) == len(other.cards):
			return self.cards[-1] > other.cards[-1]

		return len(self.cards) > len(other.cards)

	def __str__(self):
		if len(self.cards) == 3:
			return 'tierce'
		if len(self.cards) == 4:
			return 'quarte'
		if len(self.cards) == 5:
			return 'quinte'