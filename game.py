from player import Player
from team import Team
from belote import Belote
from deck import Deck
from dealer import Dealer
from announcement import Announcement
import random
from consecutive import Consecutive

list_of_contracts = ["s","d","h","c","No trumps","All trumps"]


class Game:
    def __init__(self,team_one,team_two):
        if type(team_one) is not Team or type(team_two) is not Team:
            raise TypeError('Invalid input for team')
        if team_one.different_players(team_two) is False:
            raise TypeError('Teams cannot be created with commom players')
        self.team_one = team_one
        self.team_two = team_two
        self.table_players = [self.team_one.first,self.team_two.first,self.team_one.second,self.team_two.second]
        self.deck = Deck()
        self.round_contract = ""

    def play(self):
        len1 = len(self.team_one.name) + 10
        len2 = len(self.team_two.name) + 10
        total_len = len1 + len2 + 1

        with open('result.txt', 'w') as result_file:
            result_file.write(f'{self.team_one.name.center(len1)}|{self.team_two.name.center(len2)}')
            result_file.write(f'{total_len*'='}')
            while self.team_one.wins < 2 and self.team_two.wins < 2:
                self.run_game(result_file)
                result_file.write(f'{total_len*'='}')
                result_file.write(f'({self.team_one.wins})'.center(len1)+'|'+f'({self.team_two.wins})'.center(len2))
                result_file.write(f'{total_len*'='}')

    def run_game(self, result_file):
        team_one_score, team_two_score = 0
        while team_two_score < 151 and team_two_score < 151:
            tpl = self.round()
            
            if team_one_score == 0:
                result_file.write(f'{tpl[0]}'.ljust(17))
            else:
                result_file.write(f'{team_one_score} + {tpl[0]}'.ljust(17))
            if team_one_score == 0:
                result_file.write(f'{tpl[1]}'.ljust(17))
            else:
                result_file.write(f'{team_two_score} + {tpl[1]}'.ljust(17))
            
            team_one_score += tpl[0]
            team_two_score += tpl[1]
        if team_one_score > team_two_score:
            self.team_one.increment_wins()
        else:
            self.team_two.increment_wins()


    def choose_contract(self):
        self.round_contract = random.choice(list_of_contracts)

    def spin_players(self):
        gamer = self.table_players[0]
        self.table_players = self.table_players[1:]
        self.table_players.append(gamer)

    def round(self):
        Dealer.shuffle_deck(self.deck)
        first_dealing = Dealer.first(deck)
        second_dealing = Dealer.second(deck)
        for i in range(len(self.table_players)):
            self.table_players[i].get_cards(first_dealing[i])
            self.table_players[i].get_cards(second_dealing[i])
        t1_annoncements = self.team_one.get_announcements()
        t2_annoncements = self.team_two.get_announcements()
        self.filter_announcements(t1_annoncements)
        self.filter_announcements(t2_annoncements)
        self.compare_announcements(t1_annoncements,t2_annoncements)
        self.spin_players()
        t1_score = self.get_score_of_round(t1_announcements)
        t2_score = self.get_score_of_round(t2_announcements)
        return t1_score, t2_score


    def filter_announcement(self,team_announcements):
        if round_contract == "No trumps":
            team_announcements = []
        elif round_contract == "All trumps":
            return
        else:
            for i in range(len(team_announcements)):
                if type(team_announcements[i]) is Belote:
                    if team_announcements[i].cards[0].suit == self.round_contract:
                        del team_announcements[i]
                        i-=1

    def compare_announcements(self,t1_an,t2_an):
        if len(t1_an) == 0 or len(t2_an) == 0:
            return
        i, j = 0
        while i < len(t1_an) and type(t1_an[i]) != Consecutive:
            i+=1
        while j < len(t2_an) and type(t2_an[j]) != Consecutive:
            j+=1
        if t1_an[i].equal_power(t2_an[j]):
            self.delete_consecutive(t1_an)
            self.delete_consecutive(t2_an)
        if t1_an[i].__gt__(t2_an[j]):
            self.delete_consecutive(t2_an)
        if t2_an[j].__gt__(t1_an[i]):
            self.delete_consecutive(t1_an)


    def delete_consecutive(self,announcements):
        for i in range(len(announcements)):
            if type(announcements[i]) is Consecutive:
                del announcements[i]
                i-=1

    def get_score_of_round(self,announcements):
        score = 0
        for i in range(len(announcements)):
            score += int(announcements[i])
        return score

    def print_table_players(self):
        table = ""
        for i in range(len(self.table_players)):
            table += self.table_players[i].name + " "
        return table







