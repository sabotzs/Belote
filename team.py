from player import Player

class Team:
    def __init__(self, name, first, second):
        if not isinstance(first, Player):
            raise TypeError("Invalid type, expected Player.")
        if not isinstance(second, Player):
            raise TypeError("Invalid type, expected Player.")

        self.name = name
        self.first = first
        self.second = second
        self.wins = 0

    def get_announcements(self):
        announcements = self.first.announcements
        
        for ann in self.second.announcements:
            announcements.append(ann)

        announcements = sorted(announcements, key = lambda a: int(a), reversed = True)

        return announcements

    def increment_wins(self):
        self.wins+=1

    def __eq__(self,other):
        if self.name == other.name and self.first == other.first and self.second == other.second:
            return True
        return False

    def different_players(self,other):
        if self.first == other.first or self.second == other.second or self.second == other.first or self.second == other.second:
            return False
        return True

