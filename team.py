from players import Player

class Team:
    def __init__(self,name,first,second):
        if type(name) is not str:
            raise TypeError('Only strings are alowed for team names')
        if not isinstance(first, Player):
            raise TypeError("Invalid type, expected Player.")
        if not isinstance(second, Player):
            raise TypeError("Invalid type, expected Player.")
        
        self.name = name
        self.first = first_player
        self.second = second_player

    def get_announcements(self):
        announcements = self.first.announcements

        for ann in self.second.announcements:
            announcements.append(ann)

        return announcements
