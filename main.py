import sys
print(sys.argv)
from game import Game
from player import Player
from team import Team

def play_game(team_one_name,team_two_name,t1_name_1,t1_name_2,t2_name_1,t2_name_2):
    team_one = Team(team_two_name,Player(t1_name_1),Player(t1_name_2))
    team_two = Team(team_two_name,Player(t2_name_1),Player(t2_name_2))
    game = Game(team_one,team_two)



def main():
    t1_name = input ("Team one name: ")
    t2_name = input ("Team two name: ")
    names_t1_players = input(t1_name+ " players: ")
    names_t2_players = input(t2_name+ " players: ")
    arg_for_names_one = names_t1_players.split(" ")
    arg_for_names_two = names_t2_players.split(" ")
    if len(arg_for_names_two) != 2 or len(arg_for_names_one) != 2:
        print('Wrong input for names of players')
    else:
        play_game(t1_name,t2_name,arg_for_names_one[0],arg_for_names_one[1],arg_for_names_two[0],arg_for_names_two[1])

if __name__ == '__main__':
    main()
