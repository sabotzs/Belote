from card import Card

class Player:
   def check_all_elements_are_cards(self,lst):
        for i in range(0,len(lst)):
            if type(lst[i]) is not Card:
                return False
        return True

    def __init__(self,name,list_of_cards):
        if type(name) is not str:
            raise TypeError('Only strings are allowed for name!')
        if check_all_elements_are_cards(list_of_cards) is False:
            raise TypeError('All elements must be cards!')
        self.list_of_cards = list_of_cards
        self.name = name

    def __eq__(self,other):
        return self.name == other.name

    def check_hand():
        # to be updated later 
