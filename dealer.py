from deck import Deck
from random import shuffle

class Dealer:
	@staticmethod
	def shuffle_deck(deck):
		shuffle(deck)

	@staticmethod
	def first(deck):
		hands = ([],[],[],[])
		to_deal = deck[:20]

		for hand in hands:
			for j in range(3):
				hand.append(to_deal[0])
				to_deal = to_deal[1:]
		for hand in hands:
			for j in range(2):
				hand.append(to_deal[0])
				to_deal = to_deal[1:]

		return hands

	@staticmethod
	def second(deck):
		hands = ([],[],[],[])
		to_deal = deck[20:]

		for hand in hands:
			for j in range(3):
				hand.append(to_deal[0])
				to_deal = to_deal[1:]
		
		return hands