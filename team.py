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

    def get_announcements(self):
        announcements = self.first.announcements
        
        for ann in self.second.announcements:
            announcements.append(ann)

        return announcements
