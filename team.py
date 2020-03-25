from players import Player

class Team:
    def __init__(self,name,first_player,second_player):
        if type(name) is not str:
            raise TypeError('Only strings are alowed for team names')
        if type(first_player) is not Player:
            raise TypeError('Only players are allowed!')
        if type(second_player) is not Player:
            raise TypeError('Only players are allowed!')
        self,name = name
        self.first_player = first_player
        self.second_player = second_player
