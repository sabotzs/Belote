from consecutive import Consecutive
from carre import Carre
from belote import Belote
from card import list_of_faces
from carre import Carre


class Announcement:
    def get_consecutives(self, hand):
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
            for i in range(len(suit)-1):
                if suit[i].face == 'Q' and suit[i+1].face == 'K':
                    element = Belote([suit[i],suit[i+1]])
                    belotes.append(element)
        
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
        for carre_idx in range(len(carres)):
            for consec_idx in range(len(consecs)):
                intersection = list(set(carres[carre_idx].cards) & set(consecs[consec_idx].cards))
                if len(intersection) == 1:
                    if len(consecs[consec_idx].cards) < 5:
                        del consecs[consec_idx]
                        --consec_idx
                    elif intersection[0].face == '9'or intersection[0].face == 'J':
                        del consecs[consec_idx]
                        --consec_idx
                    else:
                        del carres[carre_idx]
                        --carre_idx

    def get_announcements(self,hand):
        consecutives = self.get_consecutives(hand)
        carres = self.get_carres(hand)
        self.check_consecutive_and_carres(consecutives, carres)

        announcements = self.get_belotes(hand)
        for consec in consecutives:
            announcements.append(consec)
        for carre in carres:
            announcements.append(carre)
        return announcements

    def are_consecutive(self, first, second):
        for i in range(len(list_of_faces)):
            if first.face == list_of_faces[i]:
                first_idx = i
            if second.face == list_of_faces[i]:
                second_idx = i

        return second_idx - first_idx == 1