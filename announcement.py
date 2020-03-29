from consecutive import Consecutive
from card import list_of_faces

class Announcement:
    def get_consecutive(self,hand):
        cons = []
        for suit in hand:
            counter = 1
            last_idx = 0 
            for i in range(0,len(suit)-1):
                if self.are_consecutive(suit[i],suit[i+1]):
                    counter +=1
                elif counter > 2:
                    elem = Consecutive(suit[i - counter + 1:i+1])
                    cons.append(elem)
                    counter = 1
            if counter > 2:
                elem = Consecutive(suit[len(suit) - counter:])
                cons.append(elem)

        return cons

                
    def are_consecutive(self,first,second):
        for i in range(len(list_of_faces)):
            if first.face == list_of_faces[i]:
                first_idx = i
            if second.face == list_of_faces[i]:
                second_idx = i
        return second_idx - first_idx == 1


