from card import Card, list_of_faces, list_of_suits

class Deck:
	def __init__(self):
		self.cards = []
		for face in list_of_faces:
			for suit in list_of_suits:
				card = Card(face, suit)
				self.cards.append(card)

	def __eq__(self, other):
		return self.cards == other.cards

	def __len__(self):
		return len(self.cards)

	def __getitem__(self, index):
		return self.cards[index]

	def __setitem__(self, index, value):
		self.cards[index] = value
