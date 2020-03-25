from random import shuffle
from card import Card

class Cards():
    list_of_number = ["7","8","9","10","J","Q","K","A"]
    list_of_color = ["c","s","h","d"]
    deck = [] 
    
    def __init__(self):
        for i in range(0,len(list_of_number)):
            for j in range(0,len(list_of_color)):
                card = Card(list_of_number[i],list_of_color[j])
                deck.append(card)

    def shuffle_cards(self):
        shuffle(deck)


нещо друго сещаш ли се или да минаваме към радаване 