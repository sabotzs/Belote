list_of_faces = ['7','8','9','10','J','Q','K','A']
list_of_suits = ['c', 'd', 'h', 's']

class Card:
    def __init__(self, face, suit):
		if face not in list_of_faces:
			raise ValueError("Invalid face")
		if suit not in list_of_suits:
			raise ValueError("Invalid suit")
		
		self.face = face
		self.suit = suit

	def __str__(self):
		return self.face + self.suit

	def __repr__(self):
		return self.__str__()

	def __eq__(self, other):
		return self.face == other.face and self.suit == other.suit

	def __gt__(self, other):
		for i in range(len(list_of_faces)):
			if self.face == list_of_faces[i]:
				self_idx = i
			if other.face == list_of_faces[i]:
				other_idx = i

		return self_idx > other_idx
