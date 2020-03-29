class Carre:
	def __init__(self, cards):
		self.cards = cards

	def __int__(self):
		if self.cards[0].face == 'J':
			return 200
		if self.cards[0].face == '9':
			return 150
		else:
			return 100

	def __repr__(self):
		return 'carre'