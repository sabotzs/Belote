from cards import Cards

class Handing(Cards):
    deck = Cards()
    first_handing = []
    second_handing = []
    def __init__(self):
    def first(self):
        for j in range(0,4):
            helper = []
            for i in range(0,3):
                deck.shuffle_cards()
                helper.append(deck[i])
                deck = deck[1::]
            first_handing.append(helper)
       for j in range(0,4):
            for i in range(0,2):
                deck.shuffle_cards()
                first_handing[j].append(deck[i])
                deck = deck[1::]
        return first_handing

    def second(self):
        for j in range(0,4):
            for i in range(0,3):
                deck.shuffle_cards()
                first_handing[j].append(deck[i])
                deck = deck[1::]
        Предлагам да направим файл сега за играчите и отборите и да кача вс файлове и поотделно да правим тестове ? 




