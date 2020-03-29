from consecutive import Consecutive
from card import list_of_faces
from carre import Carre

class Announcement:
    def get_consecutive(self, hand):
        cons = []
        
        for suit in hand:
            counter = 1
            for i in range(len(suit)-1):
                if self.are_consecutive(suit[i], suit[i+1]):
                    counter += 1
                elif counter > 2:
                    element = Consecutive(suit[i - counter + 1:i + 1])
                    cons.append(element)
                    counter = 1
            if counter > 2:
                element = Consecutive(suit[len(suit)-counter:])
                cons.append(element)

        return cons

    def get_belotes(self, hand):
        belotes = []
        
        for suit in hand:
            for i in range(len(suit)+1):
                if suit[i].face == 'Q' and suit[i+1] == 'K':
                    belote.append(Belote([suit[i],suit[i+1]]))
        
        return belotes

    def get_carres(self, hand):
        carres = []

        for club in hand[0]:
            if club.face != '7' and club.face != '8':
                helper = [club]
                for i in range(1,4):
                    for card in hand[i]:
                        if card.face == club.face:
                            helper.append(card)
                if len(helper) == 4:
                    element = Carre(helper)
                    carres.append(element)

        return carres

    def check_consecutive_and_carres(self,consecs, carres):
        pass


    def get_announcements(self,hand):
        consecutive = self.get_consecutives(hand)
        carres = self.get_carres(hand)
        #TO DO
        belotes = self.get_belotes(hand)
        announcements = []
        #TO DO

    def are_consecutive(self, first, second):
        for i in range(len(list_of_faces)):
            if first.face == list_of_faces[i]:
                first_idx = i
            if second.face == list_of_faces[i]:
                second_idx = i

        return second_idx - first_idx == 1